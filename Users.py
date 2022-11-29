import random
class Users:
    def __init__(self, userName: str, userType: str, userPatience: str,
                 timeDelta: float, viewPower: int, userID: str, userDict: dict):
        """
        This function initializes the required parameters of a user
        :param userName: first name of the user
        :param userType: rigid or flexible
        :param userPatience: patient or impatient
        :param timeDelta: time spent by user in the gym
        :param viewPower: the field of view of each user
        :param userID: Unique ID assigned to each user
        :param userDict: initializes a dictionary of users
        """
        self.userName = userName
        self.userType = userType
        self.userPatience = userPatience
        self.timeDelta = timeDelta
        self.viewPower = viewPower
        self.userID = userID
        self.userDict = userDict

    def get(self, userDict, userType, userPatience, timeDelta, viewPower):
        """
        This method gets information about the user
        :param viewPower: The field of view of the user initialized from assign_properties()
        :param timeDelta: the time spent working out initialized from assign_properties()
        :param userDict: the dictionary of all users and their initialized properties from assign_properties()
        :param userType: type of user randomly assigned from assign_properties()
        :param userPatience: user patience randomly assigned from assign_properties()
        :return: current user's dictionary
        """
        userDict[self.userID] = [self.userName, userType, userPatience, viewPower, timeDelta]
        return userDict

    def set(self, elapsedTime: float):
        """
        edit time elapsed
        TODO: elapsedTime will either be gotten from class Machine or class Layout
        :param elapsedTime: time worked out till now
        :return: updated user dictionary
        """
        for key in self.userDict.keys():
            self.userDict[key][-1] += elapsedTime
        return self.userDict

    def assign_properties(self):
        """
        Assign user properties randomly
        :return: the randomly selected type and patience and assigned viewPower and initialize time delta to 0
                 and the initialized user dictionary
        """
        ironheadType = ['rigid', 'flexible']
        ironheadPat = ['patient', 'impatient']
        self.userType = random.choice(ironheadType)
        self.userPatience = random.choice(ironheadPat)
        self.timeDelta = 0
        self.viewPower = 6
        self.userDict = {}
        return self.userType, self.userPatience, self.timeDelta, self.viewPower, self.userDict


if __name__ == "__main__":
    pass
