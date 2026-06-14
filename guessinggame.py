import random

def guessing_game():
    print("=" * 40)
    print("   🎯 Number Guessing Game!")
    print("=" * 40)
    
    # Computer ek number 1-100 mein soochta hai
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print(f"1 se 100 ke beech ek number socho!")
    print(f"Tumhare paas {max_attempts} chances hain!\n")

    while attempts < max_attempts:
        guess = int(input("Tumhara guess: "))
        attempts += 1

        if guess < secret_number:
            print(f"⬆️  Zyada! ({max_attempts - attempts} chances bache)\n")
        elif guess > secret_number:
            print(f"⬇️  Kam! ({max_attempts - attempts} chances bache)\n")
        else:
            print(f"🎉 Sahi! {attempts} attempts mein jeet gaye!")
            return

    print(f"💀 Game Over! Number tha: {secret_number}")

def play_again():
    while True:
        guessing_game()
        again = input("\nDobara khelna hai? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! 👋")
            break

play_again()