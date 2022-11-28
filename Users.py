class Users:

    def __init__(self, userName: str, userType: str, userPatience: str, timeDelta: float, viewPower: int):
        self.userName = userName
        self.userPatience = userPatience
        self.timeDelta = 0.0
        self.viewPower = 6

    def get(self):
        return self.userName, self.userPatience, self.timeDelta, self.viewPower

    def set(self):
        # TODO: update time delta
        pass

    def assign_properties(self):
        # TODO: assign rigid/flexible
        # TODO: assign impatience
        pass


if __name__ == "__main__":
    pass
