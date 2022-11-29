from itertools import permutations
import numpy as np
class Layout:

    def __init__(self, totalFloors:int, totalMachines:int, machineNumber:float, machineType:str):
        self.totalFloors = totalFloors
        self.totalMachines = totalMachines
        self.machineNumber = machineNumber
        self.machineType = machineType

    def create_layout_combination(self, floor):
        # Join machines floor-wise
        # Create every possible layout depending on number of machines

        floorLayout = [list(p) for p in permutations(floor)]
        return floorLayout

    def create_machine_space(self):
        # Create ndarray depending upon floors
        # Create 3x3 numpy array
        # Add unique machine number at the centre

        floorLayout1 = []
        floorLayout2 = []

        if self.totalMachines % 2 == 0:
            floor1 = self.totalMachines/2
            floor2 = self.totalMachines - floor1
        else:
            floor1 = self.totalMachines+1/2
            floor2 = self.totalMachines - floor1

        # Create machine space for floor 1
        for i in range(len(floor1)):
            arr1 = np.array([[np.nan, np.nan, np.nan],
                            [np.nan, i + 1, np.nan],
                            [np.nan, np.nan, np.nan]])

            floorLayout1.append(arr1)

        # Create machine space for floor 2
        for i in range(len(floor2)):
            arr2 = np.array([[np.nan, np.nan, np.nan],
                            [np.nan, i + 1, np.nan],
                            [np.nan, np.nan, np.nan]])

            floorLayout2.append(arr2)

        # Creating layout combination for both floors
        self.create_layout_combination(floor=floorLayout1)
        self.create_layout_combination(floor=floorLayout2)


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