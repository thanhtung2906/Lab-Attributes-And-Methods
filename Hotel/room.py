class Room:
    def __init__(self,number:int,capacity:int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False
    def take_room(self,people):
        if self.is_taken == False and people <= self.capacity:
            self.guests = people
            self.is_taken = True
            return f'{self.guests} take room {self.number}'
        else:
            return f'Room number {self.number} is taken'
    def free_room(self):
        if self.is_taken ==  True:
            self.is_taken = False
            self.guests = 0
        else: 
            return f'Room number {self.number} is not taken'
    
        