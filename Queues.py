# for staging area, import Layout
import time


def make_queue(machine: object):
    # initialize queue for the machine
    machine.queue = [None] * 5
    return machine


def add_user_to_queue(user: object, machine: object):
    # initialize user to the machine queue
    # update User object with current_queue
    # update machine object with user

    # make the user scan here for a new machine with a smaller queue -- Layout.find_new_machine()
    if None not in machine.queue:
        return False
    # updating machine queue
    machine.queue.append(user)
    # updating users' current queue
    setattr(user, "current_queue", machine.queue)
    return True


def check_queue(machineList: object):
    # run this piece of code in a thread
    # check for impatient user
    # check if machine is empty
    time.sleep(5)
    for machine in machineList:
        for user in machine:
            if user.impatience:
                if user.currentQueueTime > user.impatientTime or user.currentQueueTime > user.thresholdTime:
                    # find new machine using Layout --->  Layout.find_new_machine(user, user.currentMachine)
                    pass


def remove_from_queue(machine: object, user: object):
    try:
        machine.queue.remove(user)
        return True
    except Exception as e:
        return False

if __name__ == '__main__':
    pass
