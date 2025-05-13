from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    subject = StringField(
        "제목", validators=[DataRequired("제목은 필수입력 항목 입니다.")]
    )
    content = TextAreaField(
        "내용", validators=[DataRequired("내용은 필수입력 항목 입니다.")]
    )


class AnswerForm(FlaskForm):
    content = TextAreaField(
        "내용", validators=[DataRequired("내용은 필수입력 항목입니다.")]
    )


# class RegisterForm(FlaskForm):
#     username = StringField(
#         "Username", validators=[DataRequired(), validators.Length(min=3, max=25)]
#     )
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField("New Password", validators=[DataRequired()])
#     passowrd_confirm = PasswordField("Repeat Password")
#     accept_rules = BooleanField("I accept the TOS", [validators.InputRequired()])
