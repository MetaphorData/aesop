import random
import string


def gen_random_str(length: int) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
