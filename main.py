import layout
import machine
import Users
import Queues


totalMachines = 10
users = []

for i in range(100):
    users.append(Users.Users(i))

chooseLayout = layout.Layout.create_layouts()

#running the simulation
for layout in chooseLayout:
    for user in users:
        machineFound = layout.Layout.find_new_machine(user, layout)
