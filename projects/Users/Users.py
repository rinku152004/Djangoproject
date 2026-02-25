class Users():
    def __init__(self, user_id, name, email):
        self._user_id = user_id
        self._name = name
        self._email = email
    @property
    def user_id(self):
        return self._user_id
    @property
    def name(self):
        return self._name
    @property
    def email(self):
        return self._email
