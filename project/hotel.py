from room import Room  # Ensure Room class is imported if in a different file

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room.number == room_number and room.is_taken == False:
                result = room.take_room(people)
                if room.is_taken:
                    self.guests += people  
                return result
        return f"Room number {room_number} does not exist"


    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number and room.is_taken == True:
                result = room.free_room()
                if not room.is_taken:
                    self.guests -= room.guests
                return result
        return f"Room number {room_number} does not exist"

    def print_status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        free_rooms_str = ', '.join(free_rooms) if free_rooms else 'None'
        taken_rooms_str = ', '.join(taken_rooms) if taken_rooms else 'None'

        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {free_rooms_str}")
        print(f"Taken rooms: {taken_rooms_str}")
