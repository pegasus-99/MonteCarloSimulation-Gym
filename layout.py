from itertools import permutations
class Layout:

    def __init__(self, totalFloors:int, totalMachines:int, machineNumber:float, machineType:str):
        self.totalFloors = totalFloors
        self.totalMachines = totalMachines
        self.machineNumber = machineNumber
        self.machineType = machineType


    test1 = [1, 2, 3, 4, 5]
    test2 = [list(p) for p in permutations(test1)]
    print(len(test2))
    print(test2)

    def create_machine_space(self):
        # Create ndarray depending upon floors
        # Create 3x3 numpy array
        # Add unique machine number at the centre
        pass

    def create_layout(self):
        # Join machines floor-wise
        # Create every possible layout depending on number of machines
        pass

    def find_new_machine(self, currentUserMachine: float, fieldOfView: int):
        # Checks current machine of user
        # Finds machine in field of view
        # Returns all machine numbers in field of view
        pass

    def get(self):
        pass

    def set(self):
        pass


if __name__ == "__main__":
    pass