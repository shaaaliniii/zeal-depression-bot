 🧠 DEPRESSION BOT — T.E.D.D.Y  
**Text-based Early Distress Detector for Youth**

Mental health concerns are a growing crisis among adolescents — with nearly **14% of teens** affected and many cases **going undetected**. Suicide is tragically the **2nd leading cause of death** among teens. **T.E.D.D.Y (Text-based Early Distress Detector for Youth)** is a web-based AI tool designed to flag early signs of distress in students’ written work, helping educators and counselors identify students in need of support.

🔗 **Live App**: [teddy-technovation.streamlit.app](https://teddy-technovation.streamlit.app)  
📖 **Blog**: [teddytechnovation.wordpress.com](https://teddytechnovation.wordpress.com)

---

## 🚀 Features

- 📝 **Text-Based Sentiment Detection**: Analyze essays or journals for depressive language
- 📄 **PDF Upload & Text Input Support**
- 🔍 **Sentence-Level Flagging**: Identifies signs of sadness, anxiety, hopelessness, etc.
- 📊 **Category-Wise Insights**: Segregated risk indicators for deeper analysis
- 🖥️ **Simple & Accessible UI** built with Streamlit
- 📚 **Educational Use Case**: Designed for teachers and counselors

---

## 📷 Screenshots

| Input View | Results Highlighting Red Flags | Category-Wise Risk Breakdown |
|-----------|-------------------------------|-------------------------------|
| ![Text Input](screenshots/input_view.png) | ![Flagged Sentences](screenshots/flagged_output.png) | ![Category Analysis](screenshots/category_output.png) |

> _Place your images in a `screenshots/` folder in the root directory and rename accordingly._

---

## 🔧 Installation & Setup (Local)

> 💡 *Use these steps if you want to run the project locally instead of using the Streamlit Cloud version.*

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shaaaliniii/zeal-depression-bot.git
cd zeal-depression-bot
2️⃣ Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy
Edit
streamlit run Main.py
🧾 Project Structure
bash
Copy
Edit
zeal-depression-bot/
├── Main.py               # Entry point for Streamlit app
├── app.py                # Helper for launching the interface
├── Brain.py              # Core NLP logic and sentiment/category classifier
├── chat.py               # Conversation and chat-based input support
├── hi.py                 # Miscellaneous support functions
├── listen.py             # Input handlers (text/PDF)
├── requirements.txt      # Python package requirements
├── README.md             # Project documentation
├── screenshots/          # Screenshots used in README
└── sample_data/          # (Optional) Sample inputs for testing
📦 Model & Dataset Info
Training Data: Synthetic essays, Reddit posts (mental health forums), anonymized student samples

ML Approach: Lexicon + keyword-matching with rules-based sentiment filtering

Libraries Used: NLTK, TextBlob, PyPDF2, Streamlit

Categories Detected:

Sadness

Hopelessness

Anxiety

Isolation

Self-blame

Irritability

🧰 Tech Stack
Layer	Technologies Used
Language	Python
Libraries	NLTK, TextBlob, PyPDF2
Frontend	Streamlit
Hosting	Streamlit Cloud / Localhost

🔮 Future Improvements
🔍 Use of transformer models (e.g., BERT) for deeper context

📈 Timeline-based sentiment analysis to track mental health over time

🌐 Multi-language and multi-format support

🛡️ Enhanced privacy and encryption for uploads

⚠️ Disclaimer
T.E.D.D.Y is not a diagnostic tool. It is an awareness and detection aid intended for educational purposes. For clinical evaluation or diagnosis, consult a licensed mental health professional.

👩‍💻 Developed By
Shalini Singh
B.Tech CSE, IIIT Naya Raipur
GitHub: @shaaaliniii

⭐ Acknowledgements
Streamlit Team

NLTK & TextBlob

Open-source mental health datasets

Mentors at Technovation

Students and teachers who inspired this idea 💡
