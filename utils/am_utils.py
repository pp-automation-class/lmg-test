import datetime
import logging
import os
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
            "url": "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com/login",
            "email": "pcs.automationclass@gmail.com",
            "password": "1234567",
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


def log_files_path(name: str) -> str:
    log_dir = os.path.join("..", "..", "temp")
    os.makedirs(log_dir, exist_ok=True)
    return os.path.join(log_dir, name)


def screenshot(page, name: str):
    screenshot_path = log_files_path(
        f"{name}{datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S%f')}.png"
    )
    page.screenshot(path=screenshot_path, full_page=True)
    logging.info(f"Screenshot saved to '{screenshot_path}'")
