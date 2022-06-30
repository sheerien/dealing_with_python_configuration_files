import yaml
import os

ROOt = os.path.dirname(os.path.realpath(__file__))
f_yaml = os.path.join(ROOt, 'config.yaml')

with open(f_yaml, "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

print(config['logLevel'])