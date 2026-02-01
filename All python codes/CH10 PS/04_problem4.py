from random import randint

class Train:

    def __init__(self, TrainNo):
        self.TrainNo = TrainNo

    def book(self, fro, to):
        print(f"Ticket is booked in Train no: {self.TrainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.TrainNo} is running on time")

    def fare(self, fro, to):
        print(f"Fare of the train no: {self.TrainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Delhi", "Mumbai")
t.getStatus()
t.fare("Delhi", "Mumbai")