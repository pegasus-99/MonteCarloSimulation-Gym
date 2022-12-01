import layout
import machine
import Users
import Queues

x = machine.Machine()
Queues.make_queue(x)
print(x.queue)