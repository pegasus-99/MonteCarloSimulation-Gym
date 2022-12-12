# for staging area, import Layout
import time
import Users
import layout
import machine
import Queues
import sys
sys.setrecursionlimit(5000)
def make_queue():
    """
    initialize queue for the machine
    :return: initial queue of none
    """
    initialQueue = [None] * 6
    return initialQueue


def add_user_to_queue(currentUser: object, currentMachine: object):
    """
    # initialize user to the machine queue
    # update User object with current_queue
    # update machine object with user
    :param currentUser: current user
    :param currentMachine: the machine user is currently wanting to use
    :return: Boolean value indicating user has been added to the queue
    """

    # make the user scan here for a new machine with a smaller queue -- Layout.find_new_machine()
    # if None not in currentMachine.queue:
    #     return False
    # updating machine queue
    currentMachine.queue.append(currentUser)
    # updating users' current queue
    currentUser.currentMachine = currentMachine
    currentUser.currentQueueTime = time.time()
    # setattr(user, "current_queue", machine.queue)
    # return True


def check_queue(machineList: object, currentLayout: object):
    """

    :param machineList: list of machines
    :return:
    """
    # run this piece of code in a thread
    # check for impatient user
    # check if machine is empty
    time.sleep(8)
    print("checking queue")
    for currentMachine in machineList:
        for user in currentMachine.queue:
            if user.impatience:
                if (time.time() - user.currentQueueTime) > user.impatientTime or user.userType == 'flexible':
                    if user.usedMachines <= 5:
                        newMachine = layout.find_new_machine(user, 5, currentLayout, currentMachine)
                        if len(newMachine.queue) == len(currentMachine.queue):
                            newMachine = layout.find_new_machine(user, None, currentLayout, currentMachine)
                        Queues.add_user_to_queue(user, newMachine)
                    # find new machine using Layout --->  Layout.find_new_machine(user, user.currentMachine)


def remove_from_queue(currentMachine: object, currentUser: object):
    """
    :param currentMachine:
    :param currentUser:
    :return:
    """
    try:
        currentMachine.queue.remove(currentUser)
        return True
    except Exception as e:
        return False


def get_best_machine(machines, currentMachine):
    """
    :param machines:
    :return:
    """
    leastQueueMachine = None
    for mach in machines:
        if not leastQueueMachine:
            leastQueueMachine = currentMachine
        elif len(mach.queue) == 0 and len(leastQueueMachine.queue) == 0:
            leastQueueMachine = currentMachine
        # it compares arrays with none values... 6, 6 dono ka len --  asically remove all nones and compare only actual values
        elif len(mach.queue) < len(leastQueueMachine.queue):
            leastQueueMachine = mach
    return leastQueueMachine


if __name__ == '__main__':
    pass
