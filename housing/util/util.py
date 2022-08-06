import yaml
from housing.exception import HousingExceptions
import os,sys


from housing.exception import HousingExceptions

def read_yaml_file(file_path:str)->dict:
    """
    Read yaml file annd returns the contents as a dictionary
    """
    try:
        with open (file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingExceptions(e,sys) from e


