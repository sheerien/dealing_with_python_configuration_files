import os 
from dotenv import load_dotenv


# Find .env file
ROOt = os.path.dirname(os.path.realpath(__file__))
f_env = os.path.join(ROOt, '.env')

# print(f_env)
load_dotenv(f_env)
# General Config
SECRET_KEY = os.environ.get('SECRET_KEY', "uhgkgh;;hklashhsakdflfg;")
FLASK_APP = os.environ.get('FLASK_APP')
FLASK_ENV = os.environ.get('FLASK_ENV')

print(SECRET_KEY)
# print(FLASK_APP)
# print(FLASK_ENV)

