from typing import (List, Union, Dict)
from uuid import uuid4

VALID_EXTENSIONS: Dict[str, bool] = {
    'png': True, 'jpeg': True, 'pdf': True, 'webp': True, 'jpg': True}


def filename_validation(filename: str) -> None:
    ''' Validates file types for lists of filenames and single file'''
    if isinstance(filename, str):
        extension: str = filename.split('.')[1]
        if extension not in VALID_EXTENSIONS:
            raise Exception('This file contains an invalid file type.')
    elif not isinstance(filename, str):
        raise Exception('filename should be a string!')


def generate_unique_name(filename: str) -> str:
    ''' Generates Unique name for Image Files '''
    if isinstance(filename, str):
        extension: str = filename.split('.')[1]
        unique_name = ''.join([str(uuid4().int)[:5] for i in range(6)])
        return unique_name + '.' + extension
    elif not isinstance(filename, str):
        raise Exception('filename should be a string!')
