import configparser
import glob
import os

default_config = configparser.ConfigParser(allow_no_value=True)
default_config.read('global_config.ini')
print(default_config.options('files'))
pattern_list = ["pipeline_config_files/*.ini"]
config_file_list = [path for pattern in pattern_list for path in glob.glob(pattern)]

for file_path in config_file_list:
    config = configparser.ConfigParser()
    basename = os.path.basename(os.path.splitext(file_path)[0])
    config.read(file_path)
    print(default_config+config)
    print(config.has_section(basename))


print(config.get('tnc_nbs_reforest', 'WORKSPACE_DIR'))
print(config.getboolean('DEFAULT', 'RUN_NDR'))
print(eval(config.get('DEFAULT', 'GLOBAL_BB')))
print(([x for x in config.options('files') if x not in config._defaults]))
