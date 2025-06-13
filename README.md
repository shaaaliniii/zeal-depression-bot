# 🧠 ZEAL Depression Bot

**ZEAL** is an AI-powered mental health assistant that detects signs of depression through natural language input. Designed especially for students and youth, it analyzes essays, journal entries, or written reflections to identify early signs of emotional distress.

Built with a lightweight Streamlit interface and NLP-powered back-end, this tool empowers teachers, counselors, and institutions to intervene early, reduce stigma, and provide timely support.

---

## 🌟 Features

- 🔍 **Text-Based Sentiment Analysis**  
  Identifies emotional tone and red-flag patterns in student-written text.

- 📂 **PDF Upload & Text Input Support**  
  Users can either type or upload documents for analysis.

- 🧠 **AI Classification Model**  
  Uses pre-trained depression classification models built with Scikit-learn.

- 📝 **Flagged Sentence Highlighting**  
  Clearly marks suspicious or high-risk sentences based on sentiment.

- 📊 **Category-Wise Analysis**  
  Sentences are grouped under risk types like: negative emotions, loneliness, etc.

- 🎨 **Clean & Intuitive UI**  
  Built using Streamlit with dynamic response rendering.

---


## 🔧 Installation & Setup (Local)

💡 Use these steps if you want to run the project locally instead of using the Streamlit Cloud version.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shaaaliniii/zeal-depression-bot.git
cd zeal-depression-bot

```
### 2️⃣ Set Up Virtual Environment (Optional but Recommended)

**🪟 On Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

🐧 On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt


```
4️⃣ Run the App with Streamlit
```bash
streamlit run Main.py

```

## 🗂️ Project Structure

```bash
zeal-depression-bot/
│
├── Main.py              # Launch point for the app
├── app.py               # Streamlit UI handler
├── chat.py              # Chatbot interaction logic
├── Brain.py             # NLP + depression classification logic
├── hi.py                # Text pre-processing (used for cleaning)
├── listen.py            # [Not used – placeholder for voice input]
│
├── model/               # ML models or scoring logic
│   └── depression_model.pkl
│
├── data/                # Sample or uploaded input text/PDFs
│   └── sample_input.pdf
│
├── utils/               # Helper scripts (if any)
│   └── text_cleaner.py
│
├── requirements.txt     # Python dependencies
└── README.md            # Project overview

```
## 💡 How It Works

1. **User Input**: Users can either paste text directly or upload a `.pdf` file.
2. **Sentence Extraction**: The system extracts individual sentences from the input.
3. **Depression Detection**: Each sentence is evaluated using a pre-trained depression detection ML model.
4. **Scoring and Flagging**: Sentences are scored based on emotional and linguistic cues using NLP libraries.
5. **Output with Explanation**: Flagged sentences are shown with contextual insights and potential need for professional referral.

---


## 🛠️ Tech Stack

| Layer       | Tools Used                        |
|-------------|----------------------------------|
| Language     | *Python 3*                        |
| Frontend     | *Streamlit (Web UI)*              |
| NLP/ML       | *NLTK, TextBlob, Scikit-learn*    |
| File Handling| *PyPDF2 for PDF input*            |
| Deployment   | *Streamlit Sharing or Localhost*  |

---

## 🔮 Future Work

- 🤖 **Upgrade to transformer-based models** like BERT or RoBERTa for more nuanced analysis.
- 📈 **Sentence scoring with probabilistic risk assessment** to indicate severity levels.
- 🌐 **Interactive dashboard** for teachers and counselors to monitor flagged content.
- 📱 **Mobile and multilingual support** to reach a broader audience.
- 🔁 **Continuous learning loop** using anonymized user feedback to improve accuracy.

---

## 🙏 Acknowledgements

- **[Streamlit](https://streamlit.io)**
- **[NLTK](https://www.nltk.org)**
- **[Scikit-learn](https://scikit-learn.org)**
- **[TextBlob](https://textblob.readthedocs.io)**
- Mental health insights inspired by **WHO**, **CDC**, and peer-reviewed academic research.


