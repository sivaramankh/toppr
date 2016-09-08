from flask_login import UserMixin
from . import login_manager, db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer , primary_key=True)
    email = db.Column('email_id',db.String(128),unique=True , index=True)
    username = db.Column('username', db.String(64), unique=True , index=True)
    password_hash = db.Column('password_hash' , db.String(128))
    is_admin = db.Column('is_admin', db.Integer)
    user_name = db.Column('name', db.String(128))
    registered_on = db.Column('member_since' , db.DateTime)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
