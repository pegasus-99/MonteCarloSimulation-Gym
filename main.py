import time

import layout
import machine
import Users
import Queues
import random
import threading

# totalMachines = 10
allUsers = []
allMachines = []
allLayouts = None
currentLayout = None


# def create_machines():
#     # Parameters:
#     # 1. Total machines
#     # 2. User input - count of each machine type
#     # 3.
#     machineList = []
#     totalMachines = int(input("Enter total number of machines"))
#     typeMachine = ["Back", "Front Upper", "Legs", "Cardiovascular"]
#     for i in range(totalMachines):
#         x = [random.choice(typeMachine)]
#         machineList.append(x)
#     return machineList


# def create_users(count_users):
#     global allUsers, allMachines
#     for i in range(count_users):
#         temp = Users.Users(i, allMachines)
#         allUsers.append(temp)
#     print(1)


# running the simulation
def gym_simulation():
    print("Simulation Started")
    global allLayouts, allUsers, currentLayout
    for layoutIter in allLayouts[1]:
        currentLayout = layout
        for userIter in allUsers:
            if user.usedMachines <= 5:
                machineFound = layout.find_new_machine(userIter, None,  layoutIter, None)
                Queues.add_user_to_queue(userIter, machineFound)

    # after adding all users to te gym:
    # thread1: check for impatient users -- run Queues.check_queue()
    impatientCheck = threading.Thread(Queues.check_queue, args=(allMachines,))
    # thread2: update machines: run Machine.check_machine()
    machineCheck = threading.Thread(machine.check_machine, args=(currentLayout, allMachines))
    # thread3: print_output from main
    printOutput = threading.Thread()
    impatientCheck.start()
    machineCheck.start()
    printOutput.start()



def print_output():
    global currentLayout
    time.sleep(20)
    # print("There are currently "+""+"users in the gym"+""+"out of which x are using the machines, z are in queue and y "
    #                                                       "are waiting/finding new machine")
    # print("Layout currently being tested is :")
    # print("Machine most used by the users is :")
    # print("Best Layout efficiency as far as now is for ") # L.E = time spent by users currently on machines/ total time
    currentUsers = 0
    usedMachines = 0
    for machineObject in allMachines:
        currentUsers += len([x for x in machineObject.queue if x is not None])
        if currentUsers > 0:
            usedMachines += 1
    print("currently the number of people in the gym either on machines or working out is: "+str(currentUsers))
    print("number of machines being used: "+str(usedMachines))
    print("layout currently being used:")
    print(currentLayout)


if __name__ == "__main__":
    # global allLayouts
    # global allMachines
    # Layout = layout.Layout(allMachines, allFloors)

    createLayoutInput = []
    workoutTypes = ['Back', "Front Upper Body", "Legs", "Cardio Vascular", "Arms"]
    for type in workoutTypes:
        correctAnswer = True
        while correctAnswer:
            try:
                machCount = int(input("Enter the number of machines for "+type+" workout: "))
                for x in range(machCount):
                    createLayoutInput.append([type, 6, 10])
                correctAnswer = False
            except ValueError:
                print("Please enter an integer for the number of machines, try again")
    layoutObject = layout.Layout(1)
    allLayouts, allMachines = layoutObject.create_layouts(createLayoutInput)

    while True:
        try:
            userCount = int(input("Enter the number of users you expect in the gym: "))
            break
        except ValueError:
            print("Please enter an integer value")

    # create_users(userCount)
    allUsers = [Users.Users(i) for i in range(userCount)]
    for user in allUsers:
        user.assign_properties(allMachines)
    gym_simulation()
    # create_machines()
