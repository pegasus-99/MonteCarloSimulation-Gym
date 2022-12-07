import random


class Users:
    ironheadType = ['rigid', 'flexible']
    ironheadPat = ['patient', 'impatient']

    def __init__(self, userID: str):
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
        self.userID = userID
        # self.userDict = userDict
        self.userType = random.choice(Users.ironheadType)
        self.userPatience = random.choice(Users.ironheadPat)
        self.timeDelta = 0
        self.viewPower = 6
        self.currentMachine = None

    def get(self):
        """
        This method gets information about the user
        :return: current user's dictionary
        """
        self.userDict[self.userID] = [self.userName, self.userType, self.userPatience, self.viewPower, self.timeDelta]
        return self.userDict

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
