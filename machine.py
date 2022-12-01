class Machine:
    def __init__(self, totalMachines, useTime, peopleCount, machineType):
        self.totalMachines = totalMachines
        self.useTime = useTime
        self.peopleCount = peopleCount
        self.machineType = machineType
        """
        current_queue: [user1, user2....] --> object queue
        """
    def get(self):
        return self.totalMachines, self.useTime, self.peopleCount, self.machineType

    def set(self):
        pass


