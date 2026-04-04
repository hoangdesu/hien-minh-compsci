# Queue = []

# Dynamically-typed language

# Initialize
# for i in range(20):
#     Queue.append(-1)

# print(Queue)

# List Comprehensive

Queue = [-1 for _ in range(20)]
print(Queue)

# head_pointer = -1
HeadPointer = -1
TailPointer = -1
NumberItems = 0


def Enqueue(num: int):
    global Queue
    global HeadPointer
    global TailPointer
    global NumberItems
    
    # for i in range(len(Queue)):
    #     if Queue[i] != -1:
    #         return False

    if NumberItems >= 20:
        return False

    if TailPointer <= -1:
        HeadPointer = 0
        TailPointer = 0
        # Queue[TailPointer] = num
    else:
        TailPointer += 1
        if TailPointer == 20:
            TailPointer = 0
        # Queue[TailPointer] = num
        
    Queue[TailPointer] = num
    NumberItems += 1
    
    print('> Current Queue:', Queue)
    return True

# print(Enqueue(2))
# print(Enqueue(5))
# print(Enqueue(9))

for i in range(15):
    print(Enqueue(i))



