#app.py: All lines with st functions within was from AI, Actual Chatting is from me. All lines containing st. (etc) is from Ai as I wanted to make a browser

import time
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import streamlit as st

st.title("Microsoft Support Assistant")

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


# Initialize session state tracking
if "step" not in st.session_state:
    st.session_state.step = "device"
if "history" not in st.session_state:
    st.session_state.history = []


def add_chat(sender, message):
    st.session_state.history.append((sender, message))


# Render chat log history
for sender, msg in st.session_state.history:
    with st.chat_message(sender.lower()):
        st.write(msg)


# --- APPLICATION FLOW ---

# 1. Device Selection
if st.session_state.step == "device":
    device_input = st.chat_input("Please enter the device you are using (e.g., Windows, Xbox, Surface):")
    if device_input:
        add_chat("User", device_input)
        device = device_input.strip().lower()

        if "windows" in device:
            st.session_state.step = "login_email"
            add_chat("Assistant", "Welcome to Microsoft Support. Please enter your Microsoft account email to log in:")
            st.rerun()
        elif "xbox" in device:
            st.session_state.step = "xbox_main"
            add_chat("Assistant", "Welcome to Xbox Support. Please describe the issue you are facing (or type 'exit' to quit):")
            st.rerun()
        else:
            add_chat("Assistant", "Device not recognized. Please type 'Windows' or 'Xbox'.")
            st.rerun()

# 2. Login Step - Email
elif st.session_state.step == "login_email":
    email_input = st.chat_input("Please enter your Microsoft account email:")
    if email_input:
        add_chat("User", email_input)
        if not email_input.strip():
            add_chat("Assistant", "Invalid input. Login failed. Please try again:")
        else:
            st.session_state.step = "login_password"
            add_chat("Assistant", "Please enter your Microsoft account password:")
            st.rerun()

# 3. Login Step - Password
elif st.session_state.step == "login_password":
    password_input = st.chat_input("Please enter your Microsoft account password:")
    if password_input:
        add_chat("User", "••••••••")
        if not password_input.strip():
            add_chat("Assistant", "Invalid input. Login failed. Please restart.")
            st.session_state.step = "device"
        else:
            st.session_state.step = "microsoft_menu"
            add_chat("Assistant", "Login successful. Welcome to Microsoft Support.\n\nPress 1 for unauthorized access\nPress 2 for currency issues\nPress 3 for settings problems\nType 'exit' to quit:")
            st.rerun()

# 4. Microsoft Main Menu
elif st.session_state.step == "microsoft_menu":
    answer_input = st.chat_input("How can I help you? (1, 2, 3, or exit):")
    if answer_input:
        add_chat("User", answer_input)
        answer = answer_input.strip().lower()

        if answer in ["exit", "quit"]:
            add_chat("Assistant", "Exiting support session. Goodbye!")
            st.session_state.step = "device"
        elif answer == "1":
            st.session_state.step = "unauthorized_access"
            add_chat("Assistant", "What activity has been noticed on your account?")
            st.rerun()
        elif answer == "2":
            st.session_state.step = "currency_issues"
            add_chat("Assistant", "Option 2 selected. Please describe the currency issue you are experiencing:")
            st.rerun()
        elif answer == "3":
            st.session_state.step = "settings_issues"
            add_chat("Assistant", "Option 3 selected. Please describe the settings problem you are facing:")
            st.rerun()
        else:
            add_chat("Assistant", "Invalid answer. Please select 1, 2, 3, or type 'exit'.")

# 5. Branch: Unauthorized Access
elif st.session_state.step == "unauthorized_access":
    unauth_input = st.chat_input("What activity has been noticed on your account?")
    if unauth_input:
        add_chat("User", unauth_input)
        tokens = process_input(unauth_input)

        if any(word in tokens for word in ["game", "hour", "games", "hours"]):
            add_chat("Assistant", "We will secure your account and investigate the unauthorized transactions immediately.")
            st.session_state.step = "microsoft_menu"
            st.rerun()
        elif any(word in tokens for word in ["money", "missing", "unauthorised", "unauthorized"]):
            st.session_state.step = "unauth_2fa"
            add_chat("Assistant", "Would you like to reset your password and enable two-factor authentication? (yes/no):")
            st.rerun()
        else:
            add_chat("Assistant", "We have logged this issue and will review your account activity.")
            st.session_state.step = "microsoft_menu"

elif st.session_state.step == "unauth_2fa":
    op1_input = st.chat_input("Enable 2FA? (yes/no):")
    if op1_input:
        add_chat("User", op1_input)
        op1 = op1_input.strip().lower()
        if op1 == "yes":
            add_chat("Assistant", "Your password has been reset. Two-factor authentication configuration has been initiated.")
        else:
            add_chat("Assistant", "We recommend enabling two-factor authentication to secure your account.")
        st.session_state.step = "microsoft_menu"
        st.rerun()

# 6. Branch: Currency Issues
elif st.session_state.step == "currency_issues":
    currency_input = st.chat_input("Describe your currency issue:")
    if currency_input:
        add_chat("User", currency_input)
        tokens = process_input(currency_input)

        if "redeem" in tokens:
            add_chat("Assistant", "We will investigate the currency redemption issue and provide a solution.")
        elif any(word in tokens for word in ["appear", "see", "show"]):
            add_chat("Assistant", "We will check your account for any discrepancies and resolve the issue.")
        elif any(word in tokens for word in ["credit", "card", "debit"]):
            add_chat("Assistant", "Please follow these steps to fix the problem:\n1. Make sure credit card details are entered correctly.\n2. Refresh your page to resolve delays.")
        else:
            add_chat("Assistant", "Thank you. Our billing team will review your account.")

        st.session_state.step = "microsoft_menu"
        st.rerun()

# 7. Branch: Settings Issues
elif st.session_state.step == "settings_issues":
    settings_input = st.chat_input("Describe your settings problem:")
    if settings_input:
        add_chat("User", settings_input)
        tokens = process_input(settings_input)

        if "privacy" in tokens:
            add_chat("Assistant", "To adjust privacy settings:\n1. Ensure your account is set to private.\n2. Restart your computer to refresh settings.")
        elif "save" in tokens:
            add_chat("Assistant", "We will investigate why your settings are not saving and provide a solution.")
        else:
            add_chat("Assistant", "Thank you. Your feedback has been recorded.")

        st.session_state.step = "microsoft_menu"
        st.rerun()

# 8. Xbox Flow
elif st.session_state.step == "xbox_main":
    problem_input = st.chat_input("Describe your Xbox issue:")
    if problem_input:
        add_chat("User", problem_input)
        problem = problem_input.strip().lower()

        if problem in ["exit", "quit"]:
            add_chat("Assistant", "Exiting support session. Goodbye!")
            st.session_state.step = "device"
            st.rerun()

        tokens = process_input(problem)

        if "redeem" in tokens or "currency" in tokens:
            st.session_state.step = "xbox_game"
            add_chat("Assistant", "We will investigate the currency redemption issue. Which game are you trying to redeem currency for?")
            st.rerun()
        elif "multiplayer" in tokens or "online" in tokens:
            add_chat("Assistant", "Troubleshooting steps:\n- Check your internet connection.\n- Restart your Xbox console.\n- Ensure your Xbox Live subscription is active.")
            st.session_state.step = "device"
        else:
            add_chat("Assistant", "Thank you for providing details. Our support team will reach out shortly.")
            st.session_state.step = "device"

elif st.session_state.step == "xbox_game":
    game_input = st.chat_input("Please enter the game name:")
    if game_input:
        add_chat("User", game_input)
        game = game_input.strip().lower()

        if "halo" in game:
            add_chat("Assistant", "We will check your account for any discrepancies related to Halo Infinite.")
        elif "forza" in game:
            add_chat("Assistant", "We will check your account for any discrepancies related to Forza Horizon 5.")
        else:
            add_chat("Assistant", f"We will check your account for issues related to {game_input.strip()}.")

        st.session_state.step = "device"
        st.rerun()