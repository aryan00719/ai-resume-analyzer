const form = document.getElementById("uploadForm");
const analyzeBtn = document.getElementById("analyzeBtn");
const jdInput = document.getElementById("jd");

const progressBar = document.getElementById("progressBar");
const matchedSkillsDiv = document.getElementById("matchedSkills");
const missingSkillsDiv = document.getElementById("missingSkills");

let resumeSkills = [];

/* Resume upload */
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const file = document.getElementById("resume").files[0];
    if (!file) return alert("Upload a resume PDF");

    const formData = new FormData();
    formData.append("resume", file);

    resetUI();
    progressBar.textContent = "Processing...";

    const res = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    resumeSkills = data.skills || [];

    progressBar.textContent = "Resume Ready";
});

/* JD analysis */
analyzeBtn.addEventListener("click", async () => {
    const jdText = jdInput.value.trim();
    if (!jdText) return alert("Paste job description first");

    const res = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            resume_skills: resumeSkills,
            job_description: jdText
        })
    });

    const result = await res.json();
    renderResult(result.analysis);
});

function renderResult(analysis) {
    const score = analysis.score;
    progressBar.style.width = score + "%";
    progressBar.textContent = score + "%";

    matchedSkillsDiv.innerHTML = "";
    missingSkillsDiv.innerHTML = "";

    analysis.matched_skills.forEach(skill => {
        matchedSkillsDiv.appendChild(createSkill(skill, "matched"));
    });

    analysis.missing_skills.forEach(skill => {
        missingSkillsDiv.appendChild(createSkill(skill, "missing"));
    });
}

function createSkill(text, type) {
    const span = document.createElement("span");
    span.className = `skill ${type}`;
    span.textContent = text;
    return span;
}

function resetUI() {
    progressBar.style.width = "0%";
    progressBar.textContent = "0%";
    matchedSkillsDiv.innerHTML = "";
    missingSkillsDiv.innerHTML = "";
}