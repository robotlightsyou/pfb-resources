
friend = "Yoda"
foe = "Sidd"
# prompt user for their name

while True:
    name = input("What is your name")
    if name != '':
        break
# say hello appropriately
if name == friend:
    print("Hello", friend)
elif name == foe:
    print("I choose treason.")
else:
    print("May the force be with you,", name)
'''
friend = "Yoda"
foe = "Sidd"
# prompt user for their name
name = input("What is your name")
# say hello appropriately
if name == friend:
    print("Hello", friend)
elif name == foe:
    print("Shame")
else:
    print("May the force be with you")
    '''

