from os import environ

HIK_HOST: str = environ.get("HIK_HOST", "localhost")
HIK_USER: str | None = environ.get("HIK_USER")
HIK_PASSWORD: str | None = environ.get("HIK_PASSWORD")