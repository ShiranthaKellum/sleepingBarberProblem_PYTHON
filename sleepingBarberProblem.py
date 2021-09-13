
chairs = 5                                                                          # size of the waiting room
front = rear = count = 0                                                            # initial properties of the circular queue

def switchCase (caseNo):
    switch = {                                                                      # switch case dictionary
        1 : waitingRoom,
        2 : enqueue,
        3 : dequeue
    }
    func = switch.get (caseNo, "wrong")
    return func ()

def enqueue ():
    global count
    if count == 0:                                                                  # The 1st customer is coming to the shop
        print("\nThe barber is sleeping...zzz...zzz...")
        global rear
        rear = (rear + 1) % chairs
        count +=1
        print("The 1st customer is going to awake the barber.")

    elif count == chairs:                                                           # The shop is full
        print("\nThe waiting room is full.")
        print("The new customer is leaving")
    
    else:                                                                           # The shop is not full
        rear = (rear + 1) % chairs
        count += 1
        print("\nThe waiting room is not full.")
        print("The new customer can wait in the waiting room.")

    actions ()

def waitingRoom ():                                                                 # view the current look of the waiting room
    i = 1                                                                           # number of the customer
    print ("\n|", end="")
    for j in range (chairs):
        if i <= count:
            print ("    Customer No.", i, "   |", end= "")          
            i += 1

        else:
            print ("    Empty Chair     |", end= "")

    actions ()

def dequeue (): 
    global count    
    if count == 0:                                                                  # initially the queue is empty
        print ("\nThe shop is empty\nThe barber is sleeping...zzz...zzz...")

    else:       
        global front
        front += 1                                                                  # dequeue the front element
        count -= 1

        if count > 0:
            print ("\nOne is leaving\nThe waing room is not full")

        else:                                                                       # The last one is leaving
            print ("\nThe last customer is leaving")
            print ("The shop is empty")
            print ("The barber is going to sleep")

    actions ()

def actions ():
    print("\n\n1. Check the waiting room")                                          # set
    print("2. New customer's arrival")                                              #       of
    print("3. The barber finished one's")                                           #            actions
    print("4. Exit\n")

    action = int(input("  Action : "))

    if action != 4:
        switchCase (action)

actions ()
