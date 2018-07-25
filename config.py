import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Database setup
SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Facebook
ACCESS_TOKEN = 'EAAeeM75wM1IBAFthM0edPHacEEvd3ibsbbjSLPBNGlB7sRQFZC61eXs4cMqkHXwH7AwxcSm270whXo4o8QoRkVvLE5BEZBxyEPh6S41jyXYZCFBZCnqxVJ7VM8dUn6WSNRoKsvuTizaZAJ3DxI47W17vodFuMXZAgVZCpwnSB73uwZDZD'
VERIFY_TOKEN = 'blindchataz'

# App url
APP_URL = 'https://blindchataz.herokuapp.com/'

# For analytics purposes
CHATMETRICS_TOKEN = 'CHATMETRICS_TOKEN'

# For debugging
PAGE_ID = 'FACEBOOK_PAGE_PSID'
ADMIN_ID = "ADMIN_PSID"

