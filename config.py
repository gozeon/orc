import configparser

config = configparser.ConfigParser()
config.read('config.ini')

authConfig = config['Auth']