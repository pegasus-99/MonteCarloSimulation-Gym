from itertools import permutations
import numpy as np
class Layout:

    def __init__(self, totalFloors:int, totalMachines:int, machineNumber:float, machineType:str):
        """
        :param totalFloors:
        :param totalMachines:
        :param machineNumber:
        :param machineType:
        """
        self.totalFloors = totalFloors
        self.totalMachines = totalMachines
        self.machineNumber = machineNumber
        self.machineType = machineType

    def create_layout_combination(self, floor):
        """
        :param floor:
        :return:
        """

        # Create every possible layout depending on number of machines

        floor = [i+1 for i in range(self.totalMachines)]
        floorLayoutCombo = [list(machine) for machine in permutations(floor)]

        return floorLayoutCombo

    def create_machine_space(self):
        """
        This functions creates a 3x3 array for each machine with unique machine number at the centre.
        :return: List containing all machine arrays
        """

        # Creating empty list for floors
        floorLayout1 = []
        floorLayout2 = []

        # If machine count = even, we assign them equally to each floor
        # If machine count = odd, floor1 will have more machines than floor2


        # Row-wise layout
        # Keeping number of rows fixed = 2, columns

        if self.totalMachines % 2 == 0:
            row1 = int(self.totalMachines/2)
            row2 = int(self.totalMachines - row1)
        else:
            row1 = int((self.totalMachines+1)/2)
            row2 = int(self.totalMachines - row1)


        layoutCols = row1*3
        layoutRows = 6



        # if self.totalMachines % 2 == 0:
        #     floor1 = self.totalMachines/2
        #     floor2 = self.totalMachines - floor1
        # else:
        #     floor1 = self.totalMachines+1/2
        #     floor2 = self.totalMachines - floor1
        #
        # # Create machine space for floor 1
        # for i in range(len(floor1)):
        #     arr1 = np.array([[np.nan, np.nan, np.nan],
        #                     [np.nan, i + 1, np.nan],
        #                     [np.nan, np.nan, np.nan]])
        #
        #     floorLayout1.append(arr1)
        #
        # # Create machine space for floor 2
        # for i in range(len(floor2)):
        #     arr2 = np.array([[np.nan, np.nan, np.nan],
        #                     [np.nan, i + 1, np.nan],
        #                     [np.nan, np.nan, np.nan]])
        #
        #     floorLayout2.append(arr2)


        # Creating layout combination for both floors
        # self.create_layout_combination(floor=floorLayout1)
        # self.create_layout_combination(floor=floorLayout2)


    def find_new_machine(self, currentUserMachine: float, fieldOfView: int):
        """
        :param currentUserMachine:
        :param fieldOfView:
        :return:
        """

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