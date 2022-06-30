import os
from configparser import ConfigParser

ROOT = os.path.dirname(os.path.realpath(__file__))

f_cfg = os.path.join(ROOT, 'config.ini')

config = ConfigParser()

config.read(f_cfg)
# port = config.get('DATABASE', 'port')
# print(type(port))

print(config.has_option('DATABASE', 'port'))