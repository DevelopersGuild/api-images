from typing import (List, Union, Dict)
from uuid import uuid4

VALID_EXTENSIONS: Dict[str, bool] = {
    '.png': True, '.jpeg': True, '.pdf': True, '.webp': True}


def filename_validation(filename: Union[str, List[str]]):
    ''' Validates file types for lists of filenames and single file'''
    if isinstance(filename, str):
        extension: str = filename.split('.')[1]
        if extension not in VALID_EXTENSIONS:
            raise Exception('This file contains an invalid file type.')
    elif isinstance(filename, list):
        for name in filename:
            extension: str = filename.split('.')[1]
            if extension not in VALID_EXTENSIONS:
                raise Exception(
                    'This list contains a file with an invalid file type.')


def generate_unique_name(filename: str):
    ''' Generates Unique name for Image Files '''
    if isinstance(filename, str):
        unique_id = str(uuid4().int)[:5]
        extension: str = filename.split('.')[1]
        return 'loftly_image' + unique_id + extension
    elif isinstance(filename, list):
        return ['loftly_image' + str(uuid4().int)[:5] + filename.split('.')[1] for i in filename]
