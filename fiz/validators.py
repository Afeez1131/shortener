from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def url_validator(value):
    '''
    Url validator default from django
    '''
    value_1_invalid = False
    value_2_invalid = False 

    url_validator = URLValidator()
    try:
        url_validator(value)
    except Exception as e:
        value_1_invalid = True 
    value_2_url = 'http://' + value
    try:
        url_validator(value_2_url)
    except Exception as e:
        value_2_invalid = True
 

    if value_1_invalid == True and value_2_invalid == True:
        raise ValidationError('Incorrect URL entered')
    return value

def dot_com_validator(value):
    '''
    Validator custom to check for url contains .com
    '''
    if not '.com' in value:
        raise ValidationError('THe URL does not contain .COM')
    return value