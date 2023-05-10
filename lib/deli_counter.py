katz_deli = []

def line(deli):

    if len(deli) > 0:
        in_line = [f"{deli.index(i)+1}. {i}" for i in deli]
        in_line = " ".join(in_line)
        print(f"The line is currently: {in_line}")
    else:
        print("The line is currently empty.")

def take_a_number(deli, person):
    deli.append(person)
    print(f"Welcome, {person}. You are number {deli.index(person)+1} in line.")

def now_serving(deli):
    if len(deli) > 0:
        print(f"Currently serving {deli[0]}.")
        deli.remove(deli[0])
    else:
        print("There is nobody waiting to be served!")