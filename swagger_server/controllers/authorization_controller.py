from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
PASSWD = {"admin": "pa$$w0rd"}


def check_basicAuth(username, password, required_scopes):
    if PASSWD.get(username) == password:
        return {'username': username}

    return None


