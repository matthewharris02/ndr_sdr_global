import configparser
import glob
import os

config = configparser.ConfigParser(allow_no_value=True)
config.read('global_config.ini')

pattern_list = ["pipeline_config_files/*.ini"]
config_file_list = [path for pattern in pattern_list for path in glob.glob(pattern)]

for file_path in config_file_list:
	basename = os.path.basename(os.path.splitext(file_path)[0])
	config.read(file_path)
	print(config.has_section(basename))
