from flask import Flask
from flask_login import UserMixin, current_user, login_manager
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf.csrf import CSRFProtect

#app = Flask(__name__, template_folder='../templates')
