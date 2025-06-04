def intro():
    print("🌄 You wake up in a dark forest. There are two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    choice = input("Which path do you choose? (1/2): ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Try again.")
        intro()

def left_path():
    print("\n🌲 You walk down the left path and find a peaceful river.")
    print("You see something shiny in the water.")
    print("1. Reach into the water.")
    print("2. Ignore it and move on.")
    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print("\n💎 You pull out a glowing gem! You win!")
    elif choice == "2":
        print("\n🚶‍♂️ You keep walking and get lost in the woods. Game over.")
    else:
        print("Invalid choice. Try again.")
        left_path()

def right_path():
    print("\n🌫️ You take the right path and encounter a sleeping dragon.")
    print("1. Try to sneak past it.")
    print("2. Attack it.")
    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print("\n🐉 You sneak past quietly and find a treasure chest. You win!")
    elif choice == "2":
        print("\n🔥 The dragon wakes up and breathes fire. Game over.")
    else:
        print("Invalid choice. Try again.")
        right_path()

if __name__ == "__main__":
    intro()
