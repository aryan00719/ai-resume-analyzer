#AI Resume Analyzer & Job Match Platform

A full-stack web application that analyzes resumes and matches them against job descriptions using NLP techniques, skill normalization, and rule-based inference. The system provides an interpretable match score along with matched and missing skills to help candidates understand their job fit.

---

🚀 Features
• 📄 Upload and parse PDF resumes
• 🧠 Extract technical skills from unstructured resume text
• 🧩 Normalize skill variants (e.g., ML → Machine Learning, SQLite → SQL)
• 🔍 Infer implicit skills using rule-based NLP (e.g., scikit-learn → Machine Learning)
• 📊 Match resumes with job descriptions and compute a match score
• ✅ Highlight matched skills
• ❌ Identify missing skills
• 🎨 Clean, professional UI with progress bar and skill tags

---

🏗️ Tech Stack

Frontend
• HTML
• CSS
• JavaScript (Vanilla)

Backend
• Python
• Flask

NLP & Processing
• Keyword-based skill extraction
• Skill normalization using synonym mapping
• Rule-based skill inference
• Set-based matching logic

---

⚙️ How It Works (High Level) 1. Resume Upload
• User uploads a PDF resume
• Backend extracts raw text using pdfplumber 2. Resume Analysis
• Skills are extracted using a predefined skill vocabulary
• Skills are normalized to canonical forms
• Implicit skills (e.g., Machine Learning) are inferred using contextual indicators 3. Job Description Analysis
• Job description text is parsed
• Required skills are extracted and normalized 4. Matching Logic
• Resume skills are compared with job description skills
• Match score is calculated based on job requirements
• Missing and matched skills are identified 5. Result Visualization
• Match score shown via progress bar
• Matched skills shown in green
• Missing skills shown in red

---

📂 Project Structure

ai-resume-analyzer/
│
├── app.py
├── requirements.txt
├── utils/
│ ├── resume_parser.py
│ ├── jd_parser.py
│ ├── similarity.py
│ └── skill_normalizer.py
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── script.js
│
├── uploads/
└── README.md

▶️ How to Run Locally

1️⃣ Clone the repository
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

2️⃣ Install dependencies
python3 -m pip install -r requirements.txt

3️⃣ Run the application
python3 app.py

4️⃣ Open in browser
http://127.0.0.1:5000

---

🧪 Example Output
• Match Score: 60–90% (depends on JD)
• Matched Skills: Python, Flask, SQL, JavaScript, Machine Learning
• Missing Skills: Docker, AWS, Django (example)

The system intentionally produces conservative and explainable results rather than over-inflated scores.

---

🎯 Design Decisions
• Rule-based inference is used instead of black-box AI to ensure explainability
• Match score is based on job description requirements, not resume length
• Skill vocabulary is deliberately extensible for future improvement

---

🔮 Future Improvements
• Semantic matching using sentence embeddings
• AI-generated resume improvement suggestions
• Weighted scoring for required vs good-to-have skills
• Resume report export (PDF)
• Authentication and saved analyses

---

🎤 Interview Talking Points
• Full-stack client–server architecture
• NLP preprocessing and normalization
• Explainable skill inference
• Backend-driven business logic
• Realistic ATS-style matching system

---

📌 Author

Aryan Mishra
Computer Science Undergraduate
Interested in AI, Backend, and Full-Stack Development
