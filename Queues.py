# for staging area, import Layout
import time
import Users
import machine


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
    if None not in currentMachine.queue:
        return False
    # updating machine queue
    currentMachine.queue.append(currentUser)
    # updating users' current queue
    currentUser.currentMachine = currentMachine
    currentUser.currentQueueTime = time.time()
    # setattr(user, "current_queue", machine.queue)
    return True


def check_queue(machineList: object):
    """

    :param machineList: list of machines
    :return:
    """
    # run this piece of code in a thread
    # check for impatient user
    # check if machine is empty
    time.sleep(10)
    print("checking queue")
    for machine in machineList:
        for user in machine.queue:
            if user.impatience:
                if user.currentQueueTime > user.impatientTime:
                    # find new machine using Layout --->  Layout.find_new_machine(user, user.currentMachine)
                    pass


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


def get_best_machine(machines):
    """
    :param machines:
    :return:
    """
    leastQueueMachine = None
    noBest = False
    for mach in machines:
        if not leastQueueMachine:
            leastQueueMachine = mach
            noBest = True
        elif len(mach.queue) < len(leastQueueMachine.queue):
            leastQueueMachine = mach
            noBest = False
    if noBest:
        return None
    else:
        return leastQueueMachine


if __name__ == '__main__':
    pass
