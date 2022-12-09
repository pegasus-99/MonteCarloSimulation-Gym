import layout
import machine
import Users
import Queues
import random

# totalMachines = 10
allUsers = []
allMachines = []
allLayouts = None


def create_machines():
    # Parameters:
    # 1. Total machines
    # 2. User input - count of each machine type
    # 3.
    machineList = []
    totalMachines = int(input("Enter total number of machines"))
    typeMachine = ["Back", "Front Upper", "Legs", "Cardiovascular"]
    for i in range(totalMachines):
        x = [random.choice(typeMachine)]
        machineList.append(x)
    return machineList


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

    # after adding all users to te gym:
    # thread1: check for impatient users -- run Queues.check_queue()
    # thread2: update machines: run Machine.check_machine()
    # thread3: print_output from main


def print_output():
    print("There are currently "+""+"users in the gym"+""+"out of which x are using the machines, z are in queue and y "
                                                          "are waiting/finding new machine")
    print("Layout currently being tested is :")
    print("Machine most used by the users is :")
    print("Best Layout efficiency as far as now is for ") # L.E = time spent by users currently on machines/ total time


if __name__ == "__main__":
    global allLayouts
    global allMachines
    # Layout = layout.Layout(allMachines, allFloors)

    createLayoutInput = []
    workoutTypes = ['Back', "Front Upper Body", "Legs", "Cardio Vascular", "Arms"]
    for type in workoutTypes:
        correctAnswer = True
        while correctAnswer:
            try:
                machCount = int(input("Enter the number of machines for "+type+" workout: "))
                for x in range(machCount):
                    createLayoutInput.append([type])
                correctAnswer = False
            except ValueError:
                print("Please enter an integer for the number of machines, try again")

    allLayouts, allMachines = layout.Layout.create_layouts(createLayoutInput)
    create_users()
    # create_machines()
    pass
