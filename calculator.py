print("Calculator 🧮")

while True:
    print("\nEnter numbers one by one. Type 'done' to finish.")

    numbers = []
    while True:
        value = input("Enter a number: ")

        if value.lower() == "done":
            break

        try:
            numbers.append(float(value))
        except:
            print("That's not a number, bruh. Try again.")

    if not numbers:
        print("You entered nothing 💀")
        continue

    print("\nChoose operation: +, -, *, /")
    operation = input("Enter operation: ")

    result = numbers[0]

    for num in numbers[1:]:
        if operation == "+":
            result += num
        elif operation == "-":
            result -= num
        elif operation == "*":
            result *= num
        elif operation == "/":
            if num == 0:
                print("Division by zero detected. Skipping that number 🫠")
                continue
            result /= num
        else:
            print("Invalid operation.")
            break

    print("\nResult:", result)

    again = input("\nWanna calculate again? (yes/no): ")
    if again.lower() not in ["yes", "y"]:
        print("\nPeace out ✌")
        break
