DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "octofit_db",
        "ENFORCE_SCHEMA": False,
        "CLIENT": {
            "host": "mongodb://localhost:27017",
        }
    }
}