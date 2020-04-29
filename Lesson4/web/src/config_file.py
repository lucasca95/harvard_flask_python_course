class Config(object):
    DEBUG = False
    TESTING = False
    # 'postgresql+psycopg2://USERNAME:USERPASSWORD@BDDURL/BDDNAME'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lifyvpjerldcuq:67647e827f34da01d62ec5b598e9a2410d2af61c8052a748df65be1beca3b0b6@ec2-52-207-25-133.compute-1.amazonaws.com/d1i2njih9eei5k'
    SECRET_KEY = '!!If33lG00d!T4r4RaRar4r4rA!!'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True