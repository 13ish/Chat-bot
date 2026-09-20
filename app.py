import time
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import streamlit as st

st.write("App is loading...")

nltk.download("punkt", quiet=True)
nltk.download("wordnet", quiet=True)

lemmatizer = WordNetLemmatizer()


def process_input(text):
    """Tokenize and lemmatize user input (checking both nouns and verbs)."""
    if not text:
        return []
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token, pos="v") for token in tokens]
    lemmas = [lemmatizer.lemmatize(token, pos="n") for token in lemmas]
    return lemmas


def login():
    st.write(" ")
    st.write("Welcome to Microsoft Support. Please log in to your Microsoft account to continue.")
    st.write(" ")

    email_input = st.chat_input("Please enter your Microsoft account email: ")
    if email_input is None:
        return False
    email = email_input.strip()

    time.sleep(2)
    if not email:
        st.write(" ")
        st.write("Invalid input. Login failed.")
        st.write(" ")
        time.sleep(2)
        return False

    password_input = st.chat_input("Please enter your Microsoft account password: ")
    if password_input is None:
        return False
    password = password_input.strip()

    if not password:
        st.write(" ")
        st.write("Invalid input. Login failed.")
        st.write(" ")
        time.sleep(2)
        return False

    st.write(" ")
    st.write("Login successful. You are now logged in to your Microsoft account.\n")
    st.write(" ")
    time.sleep(2)
    return True


def microsoft():
    answer_input = st.chat_input("Welcome to Microsoft Support. How can I help you?\nPress 1 for unauthorized access\nPress 2 for currency issues\nPress 3 for settings problems\nType 'exit' to quit: ")
    if answer_input is None:
        return True

    answer = answer_input.strip().lower()

    if answer in ["exit", "quit"]:
        return False

    # Unauthorised Access Issues
    if answer == "1":
        unauthorised_input = st.chat_input("What activity has been noticed on your account? ")
        if unauthorised_input:
            tokens = process_input(unauthorised_input)
            time.sleep(2)

            if ("game" in tokens or "hour" in tokens or "games" in tokens or "hours" in tokens):
                st.write("We will secure your account and investigate the unauthorized transactions immediately.")
                time.sleep(2)
            elif any(word in tokens for word in ["money", "missing", "unauthorised", "unauthorized"]):
                op1_input = st.chat_input("Would you like to reset your password and enable two-factor authentication? (yes/no): ")
                if op1_input:
                    op1 = op1_input.strip().lower()

                    # 2FA enabled
                    if op1 == "yes":
                        st.write(" ")
                        st.write("Your password has been reset and two-factor authentication has been enabled.")
                        st.write(" ")
                        number = st.chat_input("Please provide your contact number to enable two-factor authentication: ")
                        st.write(" ")
                        st.write(f"An SMS with a verification code has been sent to {number}.")
                        st.write(" ")
                        time.sleep(2)

                        code = st.chat_input("Enter the verification code: ")
                        if code:
                            st.write(" ")
                            st.write("Two-factor authentication has been successfully enabled on your account.")
                            st.write(" ")
                            time.sleep(2)
                        else:
                            st.write(" ")
                            st.write("The verification code entered is incorrect. Please try again or contact support.")
                            st.write(" ")
                            time.sleep(2)

                    # 2FA not enabled
                    elif op1 == "no":
                        st.write(" ")
                        st.write("We recommend enabling two-factor authentication to secure your account.")
                        st.write(" ")
                        number = st.chat_input("Please provide your contact number for further assistance: " )
                        st.write(" ")
                        st.write("Thank you. Our support team will reach out to you shortly.")
                        st.write(" ")
                        time.sleep(2)

    # Currency Issues
    elif answer == "2":
        st.write("Option 2 selected.")
        st.write(" ")
        currency_issue = st.chat_input("Please describe the currency issue you are experiencing: ")
        st.write(" ")
        if currency_issue:
            tokens = process_input(currency_issue)
            time.sleep(2)

            if "redeem" in tokens:
                st.write("We will investigate the currency redemption issue and provide a solution.")
                st.write(" ")
                time.sleep(2)
            elif any(word in tokens for word in ["appear", "see", "show"]):
                st.write("We will check your account for any discrepancies and resolve the issue.")
                time.sleep(2)
            elif ( "credit" in tokens or "card" in tokens or "debit" in tokens ):
                st.write("Please follow the following steps to fix problem")
                st.write("1. Make sure that credit card details have been entered correctly ")
                st.write(" ")
                st.write("2. refresh your page. This can help it windows has recently been experiencing delay")
                st.write(" ")
                time.sleep(2)

    # Settings Issues
    elif answer == "3":
        st.write(" ")
        st.write("Option 3 selected.")
        st.write(" ")
        settings_issue = st.chat_input( "Please describe the settings problem you are facing: ")
        if settings_issue:
            tokens = process_input(settings_issue)
            time.sleep(2)

            if "privacy" in tokens:
                st.write("We will assist you in changing your privacy settings. Please follow the instructions provided.")
                st.write(" ")
                st.write("1. Make sure there account is set to private ")
                st.write(" ")
                st.write("2. make sure you refresh your windows settings by shutting off and turning on your computer")
                st.write(" ")
                time.sleep(2)
                st.write(" ")
            elif "save" in tokens:
                st.write( "We will investigate why your settings are not saving and provide a solution.")
                time.sleep(2)
                st.write(" ")

    else:
        st.write(" ")
        st.write("Invalid answer.")
        time.sleep(2)

    return True


def xbox():
    problem_input = st.chat_input('Please describe the issue you are facing with your Xbox or Xbox account (or type "exit" to quit): ')
    if problem_input is None:
        return True

    problem = problem_input.strip().lower()

    if problem in ["exit", "quit"]:
        return False

    tokens = process_input(problem)

    if "redeem" in tokens or "currency" in tokens:
        st.write(
            "We will investigate the currency redemption issue. Which game are you trying to redeem the currency for?"
        )
        game_input = st.chat_input("Please enter the game name: ")
        if game_input:
            game = game_input.strip()
            if "halo" in game.lower():
                st.write(" ")
                st.write(
                    "We will check your account for any discrepancies related to Halo Infinite."
                )
                time.sleep(2)
            elif "forza" in game.lower():
                st.write(
                    "We will check your account for any discrepancies related to Forza Horizon 5."
                )
                time.sleep(2)
            else:
                st.write(
                    f"We will check your account for issues related to {game}."
                )
                time.sleep(2)

    elif "multiplayer" in tokens or "online" in tokens:
        st.write(
            "We will assist you in troubleshooting online multiplayer issues. Please follow these steps:"
        )
        troubleshooting_steps = [
            "Check your internet connection.",
            "Restart your Xbox console.",
            "Ensure your Xbox Live subscription is active.",
        ]
        for step in troubleshooting_steps:
            st.write(f" - {step}")
            st.chat_input("Press Enter to continue...")
            time.sleep(2)
    else:
        st.write(
            "Thank you for providing the details. Our support team will reach out to you shortly."
        )
        time.sleep(2)
    return True


# Main Execution
device_input = st.chat_input(
    "Please enter the device you are using (e.g., Windows, Xbox, Surface): "
)

if device_input is not None:
    device = device_input.strip().lower()

    if "windows" in device:
        if login():
            running = microsoft()
            if not running:
                st.write("Exiting support session. Goodbye!")

    elif "xbox" in device:
        st.write("Welcome to Xbox Support")
        running = xbox()
        if not running:
            st.write("Exiting support session. Goodbye!")

    else:
        st.write(
            "Device not recognized. Please restart and select Windows or Xbox."
        )