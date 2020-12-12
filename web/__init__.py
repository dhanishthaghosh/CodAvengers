from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask (__name__,
            instance_relative_config=False,
            template_folder="./",
            static_folder="")
#app.config['SECRET_KEY'] = '91d54e9262c3491e8a22b74c2d0e2bca'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tourismdb.db'
db = SQLAlchemy(app)
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = False 
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('GMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('GMAIL_PASSWORD') 
# mail = Mail(app) 


from web import routes