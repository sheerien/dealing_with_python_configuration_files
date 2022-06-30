# """Load configuration from .toml file."""
import toml
import os

ROOt = os.path.dirname(os.path.realpath(__file__))
f_toml = os.path.join(ROOt, 'config.toml')


# Read local `config.toml` file.
config = toml.load(f_toml)
print(config['testers'][0].get('ids', '100'))