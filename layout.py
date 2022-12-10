from itertools import permutations
import numpy as np
import machine


def find_new_machine(fieldOfView: int, layout: np.ndarray, currentUserMachine: object):
    """
    :param fieldOfView:
    :param layout:
    :param currentUserMachine:
    :return:
    """

    # Find index position of current machine ID in layout
    currentMachinePosition = np.where(layout == currentUserMachine.machineID)

    nearbyMachines = []

    # Checking if machine is present on current floor
    if len(currentMachinePosition[0]) != 0:

        # Checking nearby cells in array for new machine(-3 to +3)
        for row in range(int(currentMachinePosition[0]) - fieldOfView,
                         int(currentMachinePosition[0]) + fieldOfView + 1):
            for col in range(int(currentMachinePosition[1]) - fieldOfView,
                             int(currentMachinePosition[1]) + fieldOfView + 1):

                # Index array from current machine
                try:
                    if row >= 0 and col >= 0 and not np.isnan(layout[row][col]) \
                            and layout[row][col] != currentUserMachine.machineID:

                        machineNum = layout[row][col]

                        # Call function to get machine queue length
                        # Add to dictionary as {mach: queueLength}
                        # Return machine with least queueLength
                        nearbyMachines.append(machineNum)

                except IndexError:
                    pass

        # Call best machine = queue.findBestMachine(nearbyMachines)
        # If not Call best machine , find new machine call with field of view = layout shape/2
        return nearbyMachines

    # If machine not in current floor
    else:
        print("Machine not on this floor")


class Layout:

    def __init__(self, totalFloors: int, totalMachines: int):
        """
        :param totalFloors:
        :param totalMachines:
        """
        # self.totalFloors = totalFloors
        # self.allMachines = allMachines
        # self.totalMachines = totalMachines
        self.totalFloors = totalFloors

    def create_machine_space(self, allMachines: object):
        """
        :return: number of rows:int, number of columns:int, nested list containing unique machine numbers
        """

        # Get total machines from Machine  module? Data Structure = List
        # totalMachines = self.totalMachines
        totalMachines = len(allMachines)
        totalFloors = self.totalFloors

        floorLayout = {}
        layoutCombination = {}

        for floor in range(totalFloors):
            machinesOnFloor = round(totalMachines / totalFloors)

            # Dictionary where key = floor number, val = list containing machine numbers
            # Appending current floor number as key
            if floor + 1 not in floorLayout:
                floorLayout[floor + 1] = []

            # Get total number of machines in previous floor
            try:
                lastMachine = floorLayout[floor][-1].machineID
            except KeyError:
                pass

            # Loop over data structure given from Bum
            # allMachines = [[machineID = mach+1, 10, ], [m2], [m3]]
            # for mach in range(totalMachines):
            for mach in allMachines:
                if mach.machineID <= machinesOnFloor:
                    # currentMachine = machine.Machine(machineID = mach+1, useTime= , )

                    # Add list of machines to dictionary
                    if floor + 1 == 1:
                        # floorLayout[floor + 1].append(mach + 1)
                        floorLayout[floor + 1].append(mach)
                    else:
                        # floorLayout[floor + 1].append(lastMachine + (mach + 1))
                        if mach.machineID > lastMachine:
                            floorLayout[floor + 1].append(mach)

            totalMachines = totalMachines - machinesOnFloor
            totalFloors -= 1

        for floor, machines in floorLayout.items():

            # Create permutations of machines on each floor
            machineArrangement = [list(machineNum) for machineNum in permutations(machines)]

            if floor not in layoutCombination:
                layoutCombination[floor] = machineArrangement

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

                # Row cells will be fixed = 6
                # Col cells will vary depending on no. of machines in rows
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
                            machineArea[row, col] = machines[index].machineID
                            index += 1
                        except IndexError:
                            pass

                if floor not in allLayouts:
                    allLayouts[floor] = []

                allLayouts[floor].append(machineArea)

        return allLayouts

    def get(self):
        pass

    def set(self):
        pass


if __name__ == "__main__":
    pass
