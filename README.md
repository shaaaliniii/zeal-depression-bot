# 🧠 DEPRESSION BOT —
**Text-based Early Distress Detector for Youth**

Mental health concerns are a growing crisis among adolescents — with nearly **14% of teens** affected and many cases **going undetected**. Suicide is tragically the **2nd leading cause of death** among teens. T.E.D.D.Y (Text-based Early Distress Detector for Youth) is a web-based AI tool designed to flag early signs of distress in students’ written work, helping educators and counselors identify students in need of support.


---

## 🚀 Features

📝 **Text-Based Sentiment Detection** — Analyze essays, self-reflections, or journal entries for signs of depression and distress  
📄 **Upload PDF or Paste Text** — Supports both manual input and document uploads  
🔍 **AI-Powered Sentence Highlighting** — Flags high-risk sentences across categories like hopelessness, self-blame, and withdrawal  
📊 **Category-Wise Analysis** — Displays emotional cues in different test categories (e.g., sadness, anxiety, isolation)  
📬 **Referral Support Tool** — Helps identify students for counseling follow-up  
🎨 **Streamlit Web App** — Clean, interactive, and user-friendly interface  
🧪 **Educational Use** — Built to support teachers, counselors, and school mental health initiatives

---

## 📦 Dataset & Model

- **Data Source**: Publicly available essays, Reddit mental health posts, and synthetic student reflections  
- **Preprocessing**: Tokenization, lemmatization, TF-IDF vectorization  
- **Model Type**: Logistic Regression + Rule-based NLP classifiers  
- **Output**: Sentence-wise risk detection and category-level flags  
- **Categories Detected**:  
  - Sadness  
  - Hopelessness  
  - Self-hate  
  - Social withdrawal  
  - Anxiety  
  - Anger or irritability  

---

## 🧰 Tech Stack

| Layer         | Tools Used                  |
|---------------|-----------------------------|
| Frontend      | Streamlit                   |
| Backend       | Python, Scikit-learn        |
| NLP Toolkit   | NLTK, SpaCy, TextBlob       |
| File Support  | PyPDF2 (PDF text extraction)|
| Deployment    | Streamlit Cloud             |

---

## 📁 Project Structure

TEDDY/
├── app.py # Main Streamlit application
├── model.py # ML/NLP classification logic
├── utils.py # File processing, sentence tagging
├── categories.json # Custom emotional keyword lists
├── sample_inputs/ # Example test files
├── requirements.txt # Python dependencies
└── README.md # Project overview

yaml
Copy
Edit

---

## 🔮 Future Work

- 🧠 Upgrade to Transformer-based models (e.g., BERT) for deeper contextual understanding  
- 🌐 Multi-language input support  
- 📈 Visualization of emotional trends over time  
- 🛡️ Privacy features to ensure secure analysis  
- 🧾 Downloadable reports for counselors  

---

## 🙋‍♀️ Author

**Shalini Singh**  
B.Tech Computer Science  
IIIT Naya Raipur  
[GitHub](https://github.com/shaaaliniii)

---

## ⭐ Acknowledgements

- NLTK, SpaCy, Streamlit  
- Open-source mental health datasets  
- Educators and counselors who inspired this initiative  
- Technovation Global Challenge
