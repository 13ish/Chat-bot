import time
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()


def process_input(text):
    """Tokenize and lemmatize user input (checking both nouns and verbs)."""
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token, pos='v') for token in tokens]
    lemmas = [lemmatizer.lemmatize(token, pos='n') for token in lemmas]
    return lemmas


def login():
    print(" ")
    print("Welcome to Microsoft Support. Please log in to your Microsoft account to continue.")
    print(" ")
    email = input('Please enter your Microsoft account email: ').strip()
    time.sleep(2)
    if not email:
        print(" ")
        print("Invalid input. Login failed.")
        print(" ")
        time.sleep(2)
        return False

    password = input('Please enter your Microsoft account password: ').strip()
    if not password:
        print(" ")
        print("Invalid input. Login failed.")
        print(" ")
        time.sleep(2)
        return False
    print(" ")
    print("Login successful. You are now logged in to your Microsoft account.\n")
    print(" ")
    time.sleep(2)
    return True


def microsoft():
    answer = input("Welcome to Microsoft Support. How can I help you?\nPress 1 for unauthorized access\nPress 2 for currency issues\nPress 3 for settings problems\nType 'exit' to quit: ").strip().lower()
    

    if answer in ["exit", "quit"]:
        return False

    # Unauthorised Access Issues
    if answer == "1":
        unauthorised = input("What activity has been noticed on your account? ")
        tokens = process_input(unauthorised)
        time.sleep(2)

       
        if "game" in tokens or "hour" in tokens or "games" in tokens or "hours" in tokens:
            print("We will secure your account and investigate the unauthorized transactions immediately.")
            print(" ")
            time.sleep(2)
        elif any(word in tokens for word in [ "money", "missing", "unauthorised", "unauthorized"]):
            op1 = input('Would you like to reset your password and enable two-factor authentication? (yes/no): ').strip().lower()
        
            
            # 2FA enabled
            if op1 == 'yes':   
                print(" ")
                print("Your password has been reset and two-factor authentication has been enabled.")
                print(" ")
                number = input('Please provide your contact number to enable two-factor authentication: ')
                print(" ")
                print(f'An SMS with a verification code has been sent to {number}.')
                print(" ")
                time.sleep(2)
                
                code = input("Enter the verification code: ")
                if code == code:
                    print(" ")
                    print("Two-factor authentication has been successfully enabled on your account.")
                    print(" ")
                    time.sleep(2)
                else:
                    print(" ")
                    print("The verification code entered is incorrect. Please try again or contact support.")
                    print(" ")
                    time.sleep(2)

            # 2FA not enabled
            elif op1 == 'no':
                print(" ")
                print("We recommend enabling two-factor authentication to secure your account.")
                print(" ")
                number = input("Please provide your contact number for further assistance: ")
                print(" ")
                print("Thank you. Our support team will reach out to you shortly.")
                print(" ")
                time.sleep(2)


    # Currency Issues
    elif answer == "2":
        print("Option 2 selected.")
        print(" ")
        currency_issue = input("Please describe the currency issue you are experiencing: ")
        print(" ")
        tokens = process_input(currency_issue)
        time.sleep(2)

        if "redeem" in tokens:
            print("We will investigate the currency redemption issue and provide a solution.")
            print(" ")
            time.sleep(2)
        elif any(word in tokens for word in ["appear", "see", "show"]):
            print("We will check your account for any discrepancies and resolve the issue.")
            time.sleep(2)
        elif "credit" in tokens or "card" in tokens or "debit" in tokens:
            print("Please follow the following steps to fix problem")
            print("1. Make sure that credit card details have been entered correctly ")
            print(" ")
            print("2. refresh your page. This can help it windows has recently been experiencing delay")
            print(" ")
            time.sleep(2)
    # Settings Issues       
    elif answer == "3":
        print(" ")
        print("Option 3 selected.")
        print(" ")
        settings_issue = input("Please describe the settings problem you are facing: ")
        tokens = process_input(settings_issue)
        time.sleep(2)

        if "privacy" in tokens:
            print("We will assist you in changing your privacy settings. Please follow the instructions provided.")
            print(" ")
            print('1. Make sure there account is set to private ')
            print(' ')
            print('2. make sure you refresh your windows settings by shutting off and turning on your computer')
            print(' ')
            time.sleep(2)
            print(" ")
        elif "save" in tokens:
            print("We will investigate why your settings are not saving and provide a solution.")
            time.sleep(2)
            print(" ")

    else:
        print(" ")
        print("Invalid answer.")
        time.sleep(2)
    
    return True


def xbox():
    problem = input('Please describe the issue you are facing with your Xbox or Xbox account (or type "exit" to quit): ')
    if problem.strip().lower() in ["exit", "quit"]:
        return False

    tokens = process_input(problem)

    if "redeem" in tokens or "currency" in tokens:
        print("We will investigate the currency redemption issue. Which game are you trying to redeem the currency for?")
        game = input("Please enter the game name: ").strip()
        
        if "halo" in game.lower():
            print(" ")
            print("We will check your account for any discrepancies related to Halo Infinite.")
            time.sleep(2)
        elif "forza" in game.lower():
            print("We will check your account for any discrepancies related to Forza Horizon 5.")
            time.sleep(2)
        else:
            print(f"We will check your account for issues related to {game}.")
            time.sleep(2)

    elif "multiplayer" in tokens or "online" in tokens:
        print("We will assist you in troubleshooting online multiplayer issues. Please follow these steps:")
        troubleshooting_steps = [
            "Check your internet connection.",
            "Restart your Xbox console.",
            "Ensure your Xbox Live subscription is active."
        ]
        for step in troubleshooting_steps:
            print(f" - {step}")
            input("Press Enter to continue...")
            time.sleep(2)
    else:
        print("Thank you for providing the details. Our support team will reach out to you shortly.")
        time.sleep(2)
    return True



device = input("Please enter the device you are using (e.g., Windows, Xbox, Surface): ").strip().lower()

if "windows" in device:
    if login():
        while True:
            running = microsoft()
            if not running:
                print("Exiting support session. Goodbye!")
                break
            time.sleep(1)

elif "xbox" in device:
    print("Welcome to Xbox Support")
    while True:
        running = xbox()
        if not running:
            print("Exiting support session. Goodbye!")
            break
        time.sleep(1)

else:
    print("Device not recognized. Please restart and select Windows or Xbox.")