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
        self.queue = []
        """
        current_queue: [user1, user2....] --> object queue
        """

    def reset_machine(self):
        self.machineUseStartTime = None
        self.queue = []

    def get(self):
        return self.machineID, self.useTime, self.peopleCount, self.machineType

    def set(self):
        pass

    # def user_machine(self, user):
    # user.elapsed_time += 5


def check_machine(currentLayout, machines, threadsStartTime):
    """
    :param currentLayout:
    :param machines:
    :return:
    """
    # temp = []
    while True:
        if (time.time() - threadsStartTime) >= 300:
            return

        print('checking machine')
        time.sleep(6)
        for machine in machines:
            if time.time() - machine.machineUseStartTime >= 5:
                machine.machineUseStartTime = time.time()

                try:
                    exitUser = machine.queue.pop(0)
                except IndexError:
                    print("Queue is empty")

                # exitUser.elapsedTime+=10
                exitUser.usedMachines += 1
                if exitUser.usedMachines <= 5:
                    try:
                        newMachine = layout.find_new_machine(exitUser, 5, currentLayout, machine)
                        if not newMachine:
                            newMachine = layout.find_new_machine(exitUser, None, currentLayout, machine)
                        if len(newMachine.queue) == len(machine.queue):
                            newMachine = layout.find_new_machine(exitUser, None, currentLayout, machine)
                        Queues.remove_from_queue(machine, exitUser)
                        Queues.add_user_to_queue(exitUser, newMachine)
                    except AttributeError:
                        continue
                else:
                    pass
