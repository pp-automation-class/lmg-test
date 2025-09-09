import random
import string


def random_email():
    return "".join(random.choice(string.ascii_letters) for _ in range(7)) + "@gmail.com"


def am_get_enviroment(env: str, item: str) -> str:
    environments = {
        "prod": {
            "url": "https://app.linkmygear.com/",
            "email": "0007nxjno9lr@mozmail.com",
            "password": "000r+WLLX9qwx^:>:3",
        },
        "dev": {
            "url": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com/login",
            "email": "7nxjno9lr@mozmail.com",
            "password": "r+WLLX9qwx^:>:3",
        },
        "dev-v2": {
            "url": "https://dev-v2.linkmygear.com/#/login}",
            "email": "7nxjno9lr@mozmail.com",
            "password": "r+WLLX9qwx^:>:3",
        },
    }

    environment = environments.get(env.lower())
    if not environment:
        raise ValueError(
            f"Unknown environment: {environment}. Available: prod, dev, dev-v2"
        )
    item = environment.get(item.lower())
    if not item:
        raise ValueError(f"Unknown item: {item}. Available: url, email, password")
    return item
