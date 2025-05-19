import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\Config.ini")

class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get('common info','url')
        return url

    @staticmethod
    def emails():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def adminemail():
        ademails = config.get('common info','adminemail')
        return ademails

    @staticmethod
    def adpassword():
        adpass = config.get('common info','adminpass')
        return adpass

    @staticmethod
    def passwords():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def unregisteredemail():
        unemail = config.get('common info', 'unremail')
        return unemail

    @staticmethod
    def names():
        name = config.get('common info', 'name')
        return name

    @staticmethod
    def companies():
        company = config.get('common info', 'company')
        return company