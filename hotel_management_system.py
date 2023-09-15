"""
Project Idea: "Hotel Management System"

Description: This project involves creating a hotel management system that simulates the management of a hotel. It will utilize object-oriented programming
principles to manage hotel rooms, customer reservations, and other hotel operations through objects.

Project Features:

Room Class: This class will represent hotel rooms and will have attributes such as room number, capacity, and status. It will also include methods
to reserve a room and cancel a reservation.

Customer Class: This class will represent hotel customers and will include attributes like customer name, surname, and email.

Hotel Class: This class will manage hotel-related data, including the list of hotel rooms and customer reservations. It will have methods to add new 
reservations, cancel reservations, and check room availability.

Error Handling: Implement error handling to handle incorrect user inputs. Provide appropriate error messages when incorrect room numbers or dates are entered.

File Handling: Store hotel room and reservation data in a file and implement methods to load and save data when the application starts and exits, respectively.

Room Status Visualization: Add a visual interface to display the status of hotel rooms (reserved, vacant, in need of cleaning, etc.).
"""


class Room:
    def __init__(self, room_number, capacity, status):    # status= empty, reserved
        self.room_number = room_number
        self.capacity = capacity
        self.status = status

    def reserve_room(self):
        self.status = "reserved"

    def cancel_reservation(self):
        if self.status == "reserved":
            self.status = "empty"
            print("reservation cancelled.")
        else:
            print("This room is already empty.")

    def end_of_holiday(self):
        if self.status == "reserved":
            self.status = "empty"
            print("Your holiday is finished. We'd like to see you again.")
        else:
            print("This room is already empty.")

    def show_room(self):
        print({
            "room number": self.room_number,
            "capacity": self.capacity,
            "status": self.status
        })


class Customer:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number


class Hotel:
    empty_rooms = []
    reserved_rooms = []
    rooms = empty_rooms + reserved_rooms
    customers = []

    def add_customer(self):
        new_customer = Customer(
            input("Please enter the customer's name: "),
            input("Please enter the customer's surname: "),
            input("Please enter the customer's phone number: ")
        )
        for customer in self.customers:
            if (customer.name == new_customer.name) and (customer.surname == new_customer.surname) and (customer.phone_number == new_customer.phone_number):
                print("This customer is already exist.")
        else:
            self.customers.append(new_customer)

    def add_room(self):
        room = Room(input("room number: "),
                    input("capacity: "),
                    input("status (empty, reserved): ")
                    )
        if room.status == "reserved":
            self.reserved_rooms.append(room)
        else:
            self.empty_rooms.append(room)

    def rent_room(self):
        capacity = input("Please enter the person number: ")
        room_number = input(
            "Please enter the room number that you want to rent: ")

        for room in self.empty_rooms:
            rent=False
            if (room.room_number == room_number) and (room.capacity >= capacity):
                room.reserve_room()
                self.check_room()
                print("Room rented.")
                rent=True

        if not rent:
            print("Sorry, room is not avaliable for you.")

    def check_room(self):
        for room in self.reserved_rooms:
            if room.status == "empty":
                self.reserved_rooms.remove(room)
                self.empty_rooms.append(room)

        for room in self.empty_rooms:
            if room.status == "reserved":
                self.empty_rooms.remove(room)
                self.reserved_rooms.append(room)
    
    def cancel_reservation(self):
        room_number=input("Please enter the number of room that you want to cancel its reservation: ")

        for room in self.reserved_rooms:
            if room.room_number==room_number:
                room.cancel_reservation()
                self.check_room()


hotel=Hotel()
hotel.add_customer()
hotel.add_room()
hotel.rent_room()
hotel.cancel_reservation()
