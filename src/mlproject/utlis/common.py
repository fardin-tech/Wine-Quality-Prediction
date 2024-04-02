import os
from box.exceptions import BoxValueError
from mlproject import logger
import json
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """reads yaml file and returns

    Args:
    path_to_yaml (str): path like input

    Raises:
    ValueError: if yaml file is empty
    e: empty file

    Returns:
    ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list ,verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool,optional): ignore if multiple dirs is to be created. Default to
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path,data: dict):
    """load json files data
    Args:
         path (path): path to json file
    Returns:
           ConfigBox: data a class attributes instead of dict
    """
    with open(path) as f:
        content =json.load(f)
    logger.info(f"json file loaded sucessfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any,path: Path):
    """save binary file
    Args:
        data (Any):data to be saved as binary
        path (path):path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path)-> Any:
    """load binary file
    Args:
        path (path):path to binary file
    Returns:
           Any: Object stored in the file
    """
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (path):path to binary file
    Returns:
           str: size in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
