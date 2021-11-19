"""
problem: processes a series of events from a log stream and outputs the session
durations for each user once a successful logout occurs. The function should 
return a structure format as the following:

output: { "username": "User02”, "session_duration": 5 }
"""


class LogProcessor:
    def __init__(self, init=None):
        if init is not None:
            self.__dict__.update(init)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __contains__(self, key):
        return key in self.__dict__


def parse_log(input: str) -> dict:
    """parse login and logout information from user"""

    # get info from log
    time, user, action = tuple(input.split(" "))

    # if user does not exist --> create new user
    if not _dict.__contains__(user):
        print(f"Adding New User: {user}")
        _dict[user] = {"time": time, "action": action, "duration": 0}

    # if user exists and if the user logged out --> calculate the duration
    if _dict[user] and action == "LogOutSuccessful":
        _dict[user].update({"duration": abs(int(time) - int(_dict[user]["time"]))})
        _dict[user].update({"action": action})
        return _dict[user]


if __name__ == "__main__":

    # Example of input log
    logs = """5 User10 LogInSuccessful
10 User10 LogOutSuccessful
"""
    _dict = LogProcessor()
    for line in logs.splitlines():
        print(parse_log(line))
