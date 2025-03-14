from random import randint as ra

class Train:
    From = str(input("Enter your place: "))
    To = str(input("Enter the place you wanto to go: "))
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, From, To):
        print(f"Ticket is booked in the train number: {self.trainNo} from {From} to {To}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is runnig on time")

    def getFare(self, From, To):
        print(f"Ticket is booked in the train number: {self.trainNo} from {From} to {To} is {ra(222, 5555)}")

t = Train(trainNo = ra(1, 1000))
t.book(t.From, t.To)
t.getStatus()
t.getFare(t.From, t.To)