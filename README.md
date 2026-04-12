# AI Resume Analyzer & Job Match Platform

A full-stack, AI-powered web application that analyzes resumes and matches them against job descriptions using NLP techniques, semantic embeddings, skill normalization, and rule-based inference. The tool provides clear, interpretable scores along with separated missing skills and actionable suggestions.

## 🚀 Features

- **📄 Document Parsing:** Upload and automatically parse PDF resumes.
- **🧠 Intelligent Extraction:** Extract technical skills from unstructured text and map them to standard terms (e.g., `ML` → `Machine Learning`).
- **🔗 Semantic Matching:** Compute a holistic Semantic Match Score by embedding the entire resume against the job description.
- **🎯 Weighted ATS Score:** Calculates deterministic match percentages based on required and good-to-have job skills.
- **✅ Actionable Visualizations:** Clearly distinguishes between matched, required missing, and optional missing skills.
- **💡 Smart Suggestions:** Generates immediate, rule-based suggestions on how to improve your match capability based on critical missing requirements.
- **🎨 Modern UX:** Clean, card-based interface with dual progress tracking and intuitive states.

## 🏗️ Tech Stack

**Frontend**
- HTML5, Vanilla JavaScript, CSS3
- Responsive, modern card-based UI without heavy frameworks

**Backend**
- Python, Flask
- `pdfplumber` for PDF text extraction

**NLP & Data Processing**
- Set-based deterministic matching logic
- Contextual/Rule-based skill inference
- Semantic string matching
- Keyword extraction processing pipelines

## ⚙️ How It Works (Pipeline)

1. **Extraction Pipeline (Upload Phase)**
   - User uploads a PDF resume.
   - Text is scraped locally using `pdfplumber`.
   - The NLP pipeline identifies, cleans, and normalizes skill entities.
   - Implicit skills are algorithmically inferred and appended.

2. **Analysis Pipeline (Job Match Phase)**
   - The user inputs a target Job Description.
   - The platform categorizes JD requirements into `Required` vs `Good-to-Have`.
   - **ATS Scoring Engine:** Intersects normalized user skills against categorized target skills with differential weighting.
   - **Semantic Scoring Engine:** Feeds the normalized text body into the semantic similarity engine.

3. **Presentation Layer**
   - Returns both the rigid ATS score and flexible Semantic score visually.
   - Outputs suggestions directly correlated to critical gaps in the `Required` pool.

## 📸 Screenshots

![Main Dashboard Placeholder](https://via.placeholder.com/800x450.png?text=Main+Dashboard+UI)
![Analysis Results Placeholder](https://via.placeholder.com/800x450.png?text=Dual+Score+%26+Suggestions+View)

## ▶️ Getting Started (Local Setup)

1. **Clone the repository**
   ```bash
   git clone https://github.com/aryan00719/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. **Set up the environment (Optional but Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:5000`

## 🔮 Future Improvements

- Add direct resume report export functionality (PDF).
- Introduce authentication to save and compare historical resume versions.
- Enhance the semantic matcher using local transformer models instead of lightweight heuristics.
- Add real-time JD suggestions dynamically tracking public job boards.

## 📌 Author

**Aryan Mishra**  
Computer Science Undergraduate  
*Passionate about AI, Backend, and robust Full-Stack Architecture.*
