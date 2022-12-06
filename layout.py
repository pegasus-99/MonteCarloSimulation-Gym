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


    def create_layouts(self):
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

            # Creating empty numpy array which is the machine space
            machineArea = np.empty((rows, cols,))
            machineArea[:] = np.nan

            # Initializing index value = 0
            idx = 0

            # Iterating over rows and columns of array
            for row in range(1, machineArea.shape[0], 3):
                for col in range(1, machineArea.shape[1], 3):

                    # Adding values to array by iterating over layout (list index value)
                    try:
                        machineArea[row, col] = layout[idx]
                        idx = idx + 1
                    except IndexError:
                        pass

            # Adding all possible combination of machineArea to list
            possibleLayouts.append(machineArea)

        return possibleLayouts

    def find_new_machine(self, fieldOfView: int):
        """
        Req:
        1. current layout
        2. current machine
        3. current queue length
        4. field of view - find all machines
        5. get queue length of all machines from 4

        :param fieldOfView:
        :return:
        """

        # Checks current machine of user
        # Finds machine in field of view
        # Returns all machine numbers in field of view

        possibleLayouts = self.create_layouts()

        for layout in possibleLayouts:
            # call function - If user wait time is over OR workout is complete - find new machine
            #currentUserMachine = function call
            currentUserMachine = None

            # Get array index position of current machine
            currentMachinePosition = np.where(layout == currentUserMachine)

            # Iterating over numpy array
            for row in range(layout.shape[0]):

                for col in range(layout.shape[1]):

                    # Index array from current machine
                    if row == currentMachinePosition[0] and col == currentMachinePosition[1]:
                        print(layout[row - 3: row + 4, col - 3: col + 4])


        # If user wait time is over OR workout is complete - find new machine


    def get(self):
        pass

    def set(self):
        pass


if __name__ == "__main__":
    pass