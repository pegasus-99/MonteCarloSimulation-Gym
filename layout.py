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
        #self.totalFloors = totalFloors
        self.totalMachines = totalMachines
        self.machineNumber = machineNumber
        self.machineType = machineType

    def create_machine_space(self):
        """
        :return: List containing all machine arrays
        """

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

        return layoutRows, layoutCols


    def create_layout_combination(self):
        """

        :return:
        """

        # Get machine rows and columns
        row, col = self.create_machine_space(self)



        # Create every possible layout depending on number of machines
        machines = [i + 1 for i in range(self.totalMachines)]
        floorLayout = [list(machine) for machine in permutations(machines)]

        # Add machines to machineArea
        # Create array for machine space
        machineArea = np.empty((row, col,))
        machineArea[:] = np.nan




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