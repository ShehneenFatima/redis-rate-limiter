def get_user(ip):
    user_db = {
        "127.0.0.1": {"group": "gold"},
        "192.168.1.100": {"group": "bronze"},
        "192.168.1.101": {"group": "silver"},
    }
    return user_db.get(ip, {"group": "default"})