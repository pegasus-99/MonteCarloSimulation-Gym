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
        #self.machineNumber = machineNumber
        #self.machineType = machineType

    def create_machine_space(self):


        # Row-wise layout
        # Keeping number of rows fixed = 2, columns

        if self.totalMachines % 2 == 0:
            row1 = int(self.totalMachines/2)
            row2 = int(self.totalMachines - row1)
        else:
            row1 = int((self.totalMachines+1)/2)
            row2 = int(self.totalMachines - row1)

        layoutRows = 6
        layoutCols = row1*3

        # Create every possible layout depending on number of machines
        machines = [i + 1 for i in range(self.totalMachines)]
        layoutCombination = [list(machine) for machine in permutations(machines)]

        return layoutRows, layoutCols, layoutCombination


    def create_layout(self):
        """
        Function is called in - create_layout_combination
        :param floorLayout:
        :param rowCount:
        :param colCount:
        :return:
        """

        # Get machine rows and columns
        rows, cols, layoutCombination = self.create_machine_space(self)


        possibleLayouts = []

        for layout in layoutCombination:

            # Creating empty numpy array which denotes machine space
            machineArea = np.empty((rows, cols,))
            machineArea[:] = np.nan

            # Initializing index value = 0
            idx = 0

            # Iterating over rows and columns of array
            for row in range(1, machineArea.shape[0], 3):
                for col in range(1, machineArea.shape[1], 3):

                    # Adding values to array
                    try:
                        machineArea[row, col] = layout[idx]
                        idx = idx + 1
                    except IndexError:
                        pass

            # Adding all possible combination of machineArea to list
            possibleLayouts.append(machineArea)

        return possibleLayouts



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

    def find_machine_position(machine):
        pass
if __name__ == "__main__":
    pass