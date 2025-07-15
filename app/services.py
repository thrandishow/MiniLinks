import random
import string


def generate_short_id(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))
