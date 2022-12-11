import random


class Users:
    ironheadType = ['rigid', 'flexible']
    ironheadPat = ['patient', 'impatient']
    workoutTypes = ['Back', "Front Upper Body", "Legs", "Cardio Vascular", "Arms"]
    def __init__(self, userID: str):
        """
        This function initializes the required parameters of a user
        :param userID: Unique ID assigned to each user
        """

        self.userID = userID
        # self.userDict = userDict
        self.userType = random.choice(Users.ironheadType)
        self.workoutMachines = None
        self.userPatience = random.choice(Users.ironheadPat)
        self.timeDelta = 0
        self.viewPower = 6
        self.currentMachine = None
        self.currentQueueTime = None
        self.usedMachines = 0




    @staticmethod
    def get_workout_day(possible_choices, dayToExclude):
        possible_choices = [v for v in possible_choices if v != dayToExclude]
        return random.choice(possible_choices), possible_choices

    @staticmethod
    def get_workout_machines(machines, workOutDay):
        temp = []
        for machine in machines:
            if machine.machineType == workOutDay:
                temp.append(machine)
        return temp

    def get(self):
        """
        This method gets information about the user
        :return: current user's dictionary
        """
        # self.userDict[self.userID] = [self.userName, self.userType, self.userPatience, self.viewPower, self.timeDelta]
        # return self.userDict
        pass

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

    def assign_properties(self, machines):
        """
        Assign user properties randomly
        :return: the randomly selected type and patience and assigned viewPower and initialize time delta to 0
                 and the initialized user dictionary
        """
        if self.userType == 'flexible':
            self.workoutMachines = machines
        elif self.userType == 'rigid':
            workoutDay, possibleTypes = self.get_workout_day(Users.workoutTypes, None)
            self.workoutMachines = self.get_workout_machines(machines, workoutDay)
            # while True:
            #     if len(machines) < 5:
            #         break
            #     if len(self.workoutMachines) < 5:
            #         workoutDay = self.get_workout_day(possibleTypes, workoutDay)
            #         self.workoutMachines.extend(self.get_workout_machines(machines, workoutDay))
            #     else:
            #         break


# if __name__ == "__main__":
#     pass
