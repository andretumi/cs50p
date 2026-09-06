import inflect

p = inflect.engine()

list_of_names = []
while True:
    try:
        name = str(input("Name: ")).title()
        list_of_names.append(name)
    except EOFError:
        adieu_to = p.join(list_of_names)
        print(f"\nAdieu, adieu, to {adieu_to}")
        break
