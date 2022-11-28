import random
class Users:

    def __init__(self, userName: str, userType: str, userPatience: str,
                 timeDelta: float, viewPower: int, userID: str, userDict: dict):
        self.userName = userName
        self.userType = userType
        self.userPatience = userPatience
        self.timeDelta = 0.0
        self.viewPower = 6
        self.userID = userID
        self.userDict = {}

    def get(self, userDict, userType, userPatience):
        userDict[self.userID] = [self.userName, userType, userPatience, self.viewPower, self.timeDelta]
        return userDict

    def set(self, userDict, elapsedTime: float):
        for key in userDict.keys():
            userDict[key][-1] += elapsedTime
        return userDict

    def assign_properties(self, userType, userPatience):
        # TODO: assign rigid/flexible
        # TODO: assign impatience
        type = ['rigid', 'flexible']
        pat = ['patient', 'impatient']
        userType = random.choice(type)
        userPatience = random.choice(pat)
        return userType, userPatience


if __name__ == "__main__":
    pass
