import Queues
import layout
import time


class Machine:
    def __init__(self, machineID, useTime, peopleCount, machineType):
        self.machineID = machineID
        self.useTime = useTime
        self.peopleCount = peopleCount
        self.machineType = machineType
        self.machineUseStartTime = None
        self.queue = Queues.make_queue()
        """
        current_queue: [user1, user2....] --> object queue
        """

    def get(self):
        return self.machineID, self.useTime, self.peopleCount, self.machineType

    def set(self):
        pass

    # def user_machine(self, user):
    # user.elapsed_time += 5


def check_machine(currentLayout, machines):
    """
    :param currentLayout:
    :param machines:
    :return:
    """
    # temp = []
    time.sleep(5)
    for machine in machines:
        if machine.machineUseStartTime - time.time() >= 10:
            machine.machineUseStartTime = time.time()
            exitUser = machine.queue.pop(0)
            #exitUser.elapsedTime+=10
            exitUser.usedMachines += 1
            if exitUser.usedMachines <= 5:
                newMachine = layout.find_new_machine(exitUser, 5, currentLayout,  machine)
                Queues.add_user_to_queue(exitUser, newMachine)
            else:
                pass