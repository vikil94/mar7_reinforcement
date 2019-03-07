

seating_arrangment = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def check_seat(seat_array):
    for rows in range(0, len(seat_array)):
        for seats in range(0, len(seat_array)):
            if seat_array[rows][seats] == None:
                print("Row {} seat {} is free".format(rows+1, seats+1))

def check_seat_inputs(seat_array):
        for rows in range(0, len(seat_array)):
            for seats in range(0, len(seat_array)):
                if seat_array[rows][seats] == None:
                    print("Row {} seat {} is free. Do you want to sit there? (y/n)" .format(rows+1, seats+1))
                    user_input = input()
                    if user_input == 'y':
                        print("What is your name?")
                        user_name = input()
                        seat_array[rows][seats] = user_name
                        return ''



check_seat(seating_arrangment)
check_seat_inputs(seating_arrangment)
print(seating_arrangment)
