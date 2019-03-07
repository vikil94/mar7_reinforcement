

seating_arrangment = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def check_seat(seating_arragment):
    for rows in range(0, len(seating_arragment)):
        for seats in range(0, len(seating_arragment)):
            if seating_arragment[rows][seats] == None:
                print("Row {} seat {} is free. Do you want to sit here? (y/n)".format(rows+1, seats+1))
                user_input = input()
                if user_input == 'y':
                    print("What is your name?")
                    user_name = input()
                    seating_arragment[rows][seats] = user_name
                    return ''


check_seat(seating_arrangment)
print(seating_arrangment)
