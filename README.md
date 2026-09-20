# Chat-bot

How to set up virtual enviroment, Paste these steps into console:

NOTE: there is good chance that your going to need to copy the code and run it in your own studio

step 1. 
python3 -m venv venv

step 2.
source venv/bin/activate

step 3. 
pip install streamlit

step 4. 
streamlit run app.py

If when running, it says something along the lines of nltk not working then follow these steps:

step 1. 
pip install nltk

step 2. 
source venv/bin/activate
pip install nltk

step 3. 
python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

step 4. 
streamlit run app.py