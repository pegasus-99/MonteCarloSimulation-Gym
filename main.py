import layout
import machine
import Users
import Queues

totalMachines = 10
allUsers = []
allLayouts = None


def create_machines():
    # Parameters:
    # 1. Total machines
    # 2. User input - count of each machine type
    # 3.
    pass


def create_users(count_users):
    global allUsers
    for i in range(count_users):
        allUsers.append(Users.Users(i))


# running the simulation
def gym_simulation():
    global allLayouts, allUsers
    for layout in allLayouts:
        for user in allUsers:
            machineFound = layout.Layout.find_new_machine(user, layout)


def print_output():
    print("There are currently "+""+"users in the gym"+""+"out of which x are using the machines, z are in queue and y "
                                                          "are waiting/finding new machine")
    print("Layout currently being tested is :")
    print("Machine most used by the users is :")
    print("Best Layout efficiency as far as now is for ") # L.E = time spent by users currently on machines/ total time


if __name__ == "__main__":
    global allLayouts
    allLayouts = layout.Layout.create_layouts()
    create_users()
    create_machines()
    pass
