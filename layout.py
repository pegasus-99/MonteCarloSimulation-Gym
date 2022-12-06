from itertools import permutations
import numpy as np
class Layout:

    def __init__(self, totalFloors:int, totalMachines:int):
        """
        :param totalFloors:
        :param totalMachines:
        :param machineNumber:
        :param machineType:
        """
        #self.totalFloors = totalFloors
        self.totalMachines = totalMachines

    def create_machine_space(self):
        """
        :return: number of rows:int, number of columns:int, nested list containing unique machine numbers
        """

        # Keeping number of rows fixed = 2, columns vary depending on total number of Machines
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
        This function creates machine area space for all values in layoutCombination
        :return: List containing multiple layouts (numpy arrays)
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
        This functions does the following:
        1. Checks current machine of user
        2. Finds all machines in field of view
        :param fieldOfView: how far can a user see from current machine
        :return: numpy array containing all nearby machine numbers
        """

        # Calling function
        possibleLayouts = self.create_layouts()

        for layout in possibleLayouts:
            # call function - If user wait time is over OR workout is complete - find new machine
            # currentUserMachine = function call
            currentUserMachine = None

            # Get array index position of current machine
            currentMachinePosition = np.where(layout == currentUserMachine)

            # Iterating over current layout (numpy array)
            for row in range(layout.shape[0]):
                for col in range(layout.shape[1]):
                    # Index array from current machine
                    if row == currentMachinePosition[0] and col == currentMachinePosition[1]:
                        # Finding machines from current machine
                        nearbyMachines = layout[row - fieldOfView: row + (fieldOfView+1),
                                                col - fieldOfView: col + (fieldOfView+1)]

                        # Get unique machines from layout
                        nearbyMachines = nearbyMachines[~np.isnan(nearbyMachines)]

        return nearbyMachines

    def get(self):
        pass

    def set(self):
        pass


if __name__ == "__main__":
    pass