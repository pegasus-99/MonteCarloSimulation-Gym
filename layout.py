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

        totalMachines = self.totalMachines
        totalFloors = self.totalFloors
        floorLayout = {}
        layoutCombination = {}

        for floor in range(totalFloors):
            machinesOnFloor = round(totalMachines / totalFloors)

            # Dictionary where key = floor number, val = list containing machine numbers
            if floor + 1 not in floorLayout:
                floorLayout[floor + 1] = []

            # Get total number of machines in previous floor
            try:
                lastMachine = floorLayout[floor][-1]
            except:
                pass

            for mach in range(totalMachines):
                if mach + 1 <= machinesOnFloor:
                    # Add list of machines to dictionary
                    if floor + 1 == 1:
                        floorLayout[floor + 1].append(mach + 1)
                    else:
                        floorLayout[floor + 1].append(lastMachine + mach + 1)

            totalMachines = totalMachines - machinesOnFloor
            totalFloors -= 1

        for floor, machines in floorLayout.items():

            machineArrangement = [list(machineNum) for machineNum in permutations(machines)]

            if floor not in layoutCombination:
                layoutCombination[floor] = machineArrangement
                # layoutCombination[floor].append(machineArrangement)

        return layoutCombination

    def create_layouts(self):
        """
        This function creates machine area space for all values in layoutCombination
        :return: Dict containing floor numbers as keys, multiple layouts as values (numpy arrays)
        """

        # Get floor layout
        layoutCombination = self.create_machine_space(self)

        allLayouts = {}
        for floor, machineCombo in layoutCombination.items():

            for machines in machineCombo:
                machinesOnFloor = len(machines)

                # Divide machines on floor into two rows
                if machinesOnFloor % 2 == 0:
                    row1 = int(machinesOnFloor / 2)
                    row2 = int(machinesOnFloor - row1)
                else:
                    row1 = int((machinesOnFloor + 1) / 2)
                    row2 = int(machinesOnFloor - row1)

                layoutRows = 6
                layoutCols = row1 * 3

                # Creating empty machine space
                machineArea = np.empty((layoutRows, layoutCols,))
                machineArea[:] = np.nan

                index = 0
                # Iterating over rows and columns of array
                for row in range(1, machineArea.shape[0], 3):
                    for col in range(1, machineArea.shape[1], 3):
                        # Adding values to array by iterating over layout (list index value)
                        try:
                            machineArea[row, col] = machines[index]
                            index += 1
                        except IndexError:
                            pass

                if floor not in allLayouts:
                    allLayouts[floor] = []

                allLayouts[floor].append(machineArea)

        return allLayouts

    def find_new_machine(self, fieldOfView:int):
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