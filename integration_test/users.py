def get_user(user_id):
    users = {
        1:{"name":"Alice"},
        2:{"name":"Bob"}
    }
    return users.get(user_id)