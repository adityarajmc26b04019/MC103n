def countdown(n):
    if n <= 0:         # Base Case
        print("Blastoff!")
        return
    print(n)
    countdown(n - 1)   # Recursive Step

countdown(3)