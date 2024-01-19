from flask import (
    Blueprint,
    url_for,
    render_template,
    flash,
    request,
    session,
    g,
    current_app,
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from flask_login import login_user
from datetime import timedelta

from beatoncloud import db
from beatoncloud.forms import UserCreateForm, UserLoginForm, RegisterInterestForm
from beatoncloud.models import User, InterestInfo

bp = Blueprint("auth", __name__, url_prefix="/")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route("/login/", methods=("GET", "POST"))
def login():
    form = UserLoginForm()
    if request.method == "POST" and form.validate_on_submit():
        error = None
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            error = "이메일 또는 비밀번호가 올바르지 않습니다."

        if error is None:
            session.clear()
            session["user_id"] = user.id

            if form.remember.data:
                # 로그인 상태를 유지하는 경우에만 세션을 영구적으로 설정
                session.permanent = True
                current_app.permanent_session_lifetime = timedelta(minutes=1)
            else:
                # 로그인 상태를 유지하지 않는 경우 브라우저 세션 동안만 세션 유지
                session.permanent = False

            login_user(user, remember=form.remember.data)

            return redirect(url_for("main.index"))

        flash(error)

    return render_template("auth/login.html", form=form)


@bp.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for("main.index"))


@bp.route("/signup/", methods=("GET", "POST"))
def signup():
    form = UserCreateForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            user = User(
                email=form.email.data,
                password=generate_password_hash(form.password1.data),
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.register_interest"))
        else:
            flash("이미 존재하는 사용자입니다.")
    return render_template("auth/signup.html", form=form)


@bp.route("/register_interest/", methods=("GET", "POST"))
def register_interest():
    form = RegisterInterestForm()

    if form.validate_on_submit():
        interest_info = InterestInfo(
            classic=form.classic.data,
            jazz=form.jazz.data,
            pop=form.pop.data,
            ballade=form.ballade.data,
            hiphop=form.hiphop.data,
            reggae=form.reggae.data,
            trot=form.trot.data,
            electronic=form.electronic.data,
            rock=form.rock.data,
        )

        db.session.add(interest_info)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template("select_interest.html", form=form)
