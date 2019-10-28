print("menu")
print("1 - add")
print("2 - Amend")
print("3 - Delete")
print("4 - Display")

menu_option = int(input("Enter option: "))

if menu_option == 1:
    print("Option 1 - Add selected")
elif menu_option == 2:
    print("Option 2 - Amend selected")
elif menu_option == 3:
    print("Option 3 -Delete selected")
elif menu_option == 4:
    print("Option 3 - Display selected")
else:
    print("invalid choice")
