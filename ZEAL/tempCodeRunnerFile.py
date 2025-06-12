import streamlit as st
from nltk import sent_tokenize
import pdfplumber
import nltk
from new import get_response
from danger_words import GetDangerWords, depressive_thought, potential_struggle, destructive_thought

nltk.download('punkt')

# Initialize session state to store chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display function
def Display(essay):
    if essay != "":
        sentences = sent_tokenize(essay)
        xgflags = []
        lrflags = []
        xgsflags = []
        wrflags = []


        # Load words
        concerning_words = GetDangerWords()
        depression = depressive_thought()
        struggle = potential_struggle()
        destructive = destructive_thought()

        loading = st.progress(0, text="Loading...")

        for i, sentence in enumerate(sentences, start=1):
            loading.progress(i / len(sentences), text=f"Analyzing sentence {i}/{len(sentences)}...")

            # Analyze each sentence and populate the corresponding flag lists
            xg_flags_found = AnalyzeSentence1(sentence, concerning_words)
            xgflags.extend(xg_flags_found)

            lr_flags_found = AnalyzeSentence2(sentence, struggle)
            lrflags.extend(lr_flags_found)

            xgs_flags_found = AnalyzeSentence3(sentence, depression)
            xgsflags.extend(xgs_flags_found)

            wr_flags_found = AnalyzeSentence4(sentence, destructive)
            wrflags.extend(wr_flags_found)

        loading.progress(1, text="Complete!")

        st.subheader("Results:")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.subheader("Concerning Words Test")
            ShowFlags(xgflags)

        with col2:
            st.subheader("Potential Struggles Test")
            ShowFlags(lrflags)

        with col3:
            st.subheader("Depressive Thoughts Test")
            ShowFlags(xgsflags)

        with col4:
            st.subheader("Self-Destructive Thoughts Test")
            ShowFlags(wrflags)

def AnalyzeSentence1(sentence, concerning_words):
    flags_found1 = []
    for word in concerning_words:
        if word in sentence:
            flags_found1.append(word)
    return flags_found1

def AnalyzeSentence2(sentence, struggle):
    flags_found2 = []
    for word in struggle:
        if word in sentence:
            flags_found2.append(word)
    return flags_found2

def AnalyzeSentence3(sentence, depression):
    flags_found3 = []
    for word in depression:
        if word in sentence:
            flags_found3.append(word)
    return flags_found3

def AnalyzeSentence4(sentence, destructive):
    flags_found4 = []
    for word in destructive:
        if word in sentence:
            flags_found4.append(word)
    return flags_found4


            
# Display function
def Display(essay):
    if essay != "":
        sentences = sent_tokenize(essay)
        xgflags = []
        lrflags = []
        xgsflags = []
        wrflags = []

        # Load words
        concerning_words = GetDangerWords()
        depression = depressive_thought()
        struggle = potential_struggle()
        destructive = destructive_thought()

        loading = st.progress(0, text="Loading...")

        for i, sentence in enumerate(sentences, start=1):
            loading.progress(i / len(sentences), text=f"Analyzing sentence {i}/{len(sentences)}...")

            # Analyze each sentence and populate the corresponding flag lists
            xg_flags_found = AnalyzeSentence1(sentence, concerning_words)
            xgflags.extend(xg_flags_found)

            lr_flags_found = AnalyzeSentence2(sentence, struggle)
            lrflags.extend(lr_flags_found)

            xgs_flags_found = AnalyzeSentence3(sentence, depression)
            xgsflags.extend(xgs_flags_found)

            wr_flags_found = AnalyzeSentence4(sentence, destructive)
            wrflags.extend(wr_flags_found)

        loading.progress(1, text="Complete!")

        st.subheader("Results:")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.subheader("Concerning Words Test")
            ShowFlags(xgflags,1)

        with col2:
            st.subheader("Potential Struggles Test")
            ShowFlags(lrflags,  2)

        with col3:
            st.subheader("Depressive Thoughts Test")
            ShowFlags(xgsflags, 3)

        with col4:
            st.subheader("Self-Destructive Thoughts Test")
            ShowFlags(wrflags, 4)


def ShowFlags(flaglist,column_index):
    i = 0
    string = "\n**" + "**\n"

    for flag in flaglist:
        i += 1
        string += str(i) + ". " + flag.replace("\n", " ") + "\n"

    if len(flaglist) == 0:
        string += "No red flags found!"

    string += "\n"
    st.write(string)


    
def GetPDFText(my_pdf):
    try:
        current_pdf = pdfplumber.open(my_pdf)
        data = ""
        pages = current_pdf.pages
        for page in pages:
            data += page.extract_text()
    except:
        data = ""
    return data

# Main section
st.title("Welcome to :violet[ZEAL]")
st.subheader("", anchor="welcome-to-t-e-d-d-y")
st.caption("*:violet[How to Use:]") 
st.caption("Express your feelings in one word into the provided area or upload a PDF file.")
st.caption("ZEAL will analyze the text and display potential red flags.\n")
st.caption("Explore the flagged sentences in each test category to gain insights.\n")
st.caption("*:violet[A note to our testers:] Our research shows that the sentiments expressed in actual student data are subtle. :red[For accurate results], use authentic student data, as Depression Bot's effectiveness relies on subtle sentiments expressed in real content.]")
st.write("\n")

with st.sidebar:
    st.title("Run an essay/conversation through our ZEAL TEXT ANALYZER!")
    essay = st.text_input("Express what you are feeling in one word:")
    submit = st.button("Submit Feelings", on_click=lambda:Display(essay))

    uploaded_file = st.file_uploader('Upload a PDF file expressing your emotions:', type="pdf")
    submit2 = st.button("Submit File", on_click=lambda: Display(GetPDFText(uploaded_file)))
    st.write("[Learn more about ZEAL](https://teddytechnovation.wordpress.com/)")
    st.write("[Help us improve!](https://forms.gle/eAYpKmd9udkdFUir6)")

st.title("DEPRESSION BOT")

# Create a form to take user input
with st.form(key='user_input_form'):
    user_input = st.text_input("You:")
    submit_button = st.form_submit_button("Send")

    # Process the input when the form is submitted
    if submit_button:
        if user_input.lower() == "bye":
            st.text_area("Bot:", value="Goodbye! If you have more questions, feel free to ask.", height=100, key="bot_response")
        else:
            bot_response = get_response(user_input)
            st.text_area("Bot:", value=bot_response, height=100, key="bot_response")
