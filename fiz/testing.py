import string 
import random
shorten = {}

def shorten_url(url = 'google.com', domain='fiz.co'):
    random_string = generate_random_string()
    
    if random_string in shorten:
        short_url = 'https://' + domain + '/' + random_string
        shorten[random_string] = short_url
        print(shorten)
    else:
        shorten_url(url = 'google.com', domain='fiz.co')


def generate_random_string(string_length=5):
    random_string = ''
    alpha_numerals = string.ascii_uppercase + string.ascii_lowercase + string.digits

    for _ in range(string_length):
        random_string = random_string + random.choice(alpha_numerals)

    return random_string

shorten_url(url = 'google.com', domain='fiz.co')