# read()	

Read and parse the named configuration file.

# sections()	

Return all the configuration section names.

# has_section()	

Return whether the given section exists.

# options()	

Return list of configuration options for the named section.

# has_option()	

Return whether the given option exists in the given section.

# read_file()	

Read and parse one configuration file, given as a file object.

# read_string()	

Read configuration from a given string.

# read_dict()	

Read configuration from a dictionary. Keys are section names, values are 
dictionaries with keys and values that should be present in the section.

# get()	

Return a string value for the named option.

# getint()	

Like get(), but convert value to an integer.

# getfloat()	

Like get(), but convert value to a float.

# getboolean()	

Like get(), but convert value to a boolean. Returns False or True.

# items()	

return a list of tuples with (name, value) for each option in the section.

# remove_section()	

Remove the given file section and all its options.

# remove_option()	

Remove the given option from the given section.

# set()	

Set the given option.

```python:
import configparser

config = configparser.ConfigParser()

config.read('sampleconfig.ini')

for sect in config.sections():
   print('Section:', sect)
   for k,v in config.items(sect):
      print(' {} = {}'.format(k,v))
   print()
```

# write()	

Write the configuration state in .ini format.

```python:
import configparser

config = configparser.ConfigParser()

config.add_section('Manager')

config.set('Manager', 'Name', 'Ashok Kulkarni')

config.set('Manager', 'email', 'ashok@gmail.com')

config.set('Manager', 'password', 'secret')
fp=open('test.ini','w')
config.write(fp)
fp.close()
```