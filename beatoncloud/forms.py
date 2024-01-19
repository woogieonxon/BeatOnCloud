from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email


class UserCreateForm(FlaskForm):
    email = EmailField("이메일", validators=[DataRequired(), Email()])
    password1 = PasswordField(
        "비밀번호", validators=[DataRequired(), EqualTo("password2", "비밀번호가 일치하지 않습니다")]
    )
    password2 = PasswordField("비밀번호확인", validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    email = EmailField("이메일", validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    remember = BooleanField("로그인 상태 유지")
    submit = SubmitField("로그인")


class RegisterInterestForm(FlaskForm):
    classic = BooleanField("클래식")
    jazz = BooleanField("재즈")
    pop = BooleanField("팝")
    ballade = BooleanField("발라드")
    hiphop = BooleanField("힙합")
    reggae = BooleanField("레게")
    trot = BooleanField("트로트")
    electronic = BooleanField("일렉트로닉")
    rock = BooleanField("락")
    rnb = BooleanField("R&B")
