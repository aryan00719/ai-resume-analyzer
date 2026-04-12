const form = document.getElementById("uploadForm");
const uploadBtn = document.getElementById("uploadBtn");
const uploadStatus = document.getElementById("uploadStatus");

const analyzeBtn = document.getElementById("analyzeBtn");
const analyzeStatus = document.getElementById("analyzeStatus");
const jdInput = document.getElementById("jd");

const atsProgressBar = document.getElementById("atsProgressBar");
const semanticProgressBar = document.getElementById("semanticProgressBar");

const matchedSkillsDiv = document.getElementById("matchedSkills");
const missingRequiredSkillsDiv = document.getElementById("missingRequiredSkills");
const missingGoodSkillsDiv = document.getElementById("missingGoodSkills");

const suggestionsBox = document.getElementById("suggestionsBox");
const suggestionsText = document.getElementById("suggestionsText");

let resumeSkills = [];
let resumeText = "";

/* Resume upload */
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const file = document.getElementById("resume").files[0];
    if (!file) return alert("Upload a resume PDF");

    const formData = new FormData();
    formData.append("resume", file);

    resetUI();
    
    uploadBtn.disabled = true;
    uploadStatus.classList.remove("hidden");
    uploadStatus.textContent = "Parsing resume...";

    try {
        const res = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        if (!res.ok) {
            throw new Error("Failed to process resume");
        }

        const data = await res.json();
        resumeSkills = data.skills || [];
        resumeText = data.resume_text || "";

        uploadStatus.textContent = "Resume parsed successfully! You can now analyze.";
        uploadStatus.style.color = "#10b981"; // Success green
    } catch (err) {
        uploadStatus.textContent = "Error parsing resume.";
        uploadStatus.style.color = "#ef4444"; // Error red
    } finally {
        uploadBtn.disabled = false;
    }
});

/* JD analysis */
analyzeBtn.addEventListener("click", async () => {
    const jdText = jdInput.value.trim();
    if (!jdText) return alert("Please paste a job description first.");
    if (resumeSkills.length === 0) return alert("Please upload and process a resume first.");

    analyzeBtn.disabled = true;
    analyzeStatus.classList.remove("hidden");
    analyzeStatus.textContent = "Analyzing against job description...";

    try {
        const res = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                resume_skills: resumeSkills,
                resume_text: resumeText,
                job_description: jdText
            })
        });

        if (!res.ok) {
            throw new Error("Analysis failed");
        }

        const result = await res.json();
        renderResult(result);
        analyzeStatus.textContent = "Analysis complete!";
        analyzeStatus.style.color = "#10b981";
    } catch (err) {
        analyzeStatus.textContent = "Error analyzing resume.";
        analyzeStatus.style.color = "#ef4444";
    } finally {
        analyzeBtn.disabled = false;
        setTimeout(() => {
            analyzeStatus.classList.add("hidden");
            analyzeStatus.style.color = "#64748b"; // reset color
        }, 3000);
    }
});

function renderResult(result) {
    const analysis = result.analysis;
    
    // Scores
    const atsScore = analysis.score;
    atsProgressBar.style.width = atsScore + "%";
    atsProgressBar.textContent = atsScore + "%";

    const semanticScore = result.semantic_score || 0;
    semanticProgressBar.style.width = semanticScore + "%";
    semanticProgressBar.textContent = semanticScore + "%";

    // Clear old skills
    matchedSkillsDiv.innerHTML = "";
    missingRequiredSkillsDiv.innerHTML = "";
    missingGoodSkillsDiv.innerHTML = "";

    // Matched
    if (analysis.matched_skills && analysis.matched_skills.length > 0) {
        analysis.matched_skills.forEach(skill => {
            matchedSkillsDiv.appendChild(createSkill(skill, "matched"));
        });
    } else {
        matchedSkillsDiv.innerHTML = "<span style='color: #64748b; font-size: 0.9rem;'>No matching skills found.</span>";
    }

    // Missing Required
    if (analysis.missing_required && analysis.missing_required.length > 0) {
        analysis.missing_required.forEach(skill => {
            missingRequiredSkillsDiv.appendChild(createSkill(skill, "missing-req"));
        });
        
        // Show Suggestions
        suggestionsBox.classList.remove("hidden");
        const missingReqStr = analysis.missing_required.join(", ");
        suggestionsText.textContent = `You are missing the following REQUIRED skills: ${missingReqStr}. Consider adding these to your resume or cover letter for a significantly better match.`;
    } else {
        missingRequiredSkillsDiv.innerHTML = "<span style='color: #64748b; font-size: 0.9rem;'>You meet all required skills!</span>";
        
        // Positive suggestion
        suggestionsBox.classList.remove("hidden");
        suggestionsText.textContent = `Great job! You have all the required skills for this position. Focus on highlighting your experience with these tools.`;
    }

    // Missing Good-to-have
    if (analysis.missing_good_to_have && analysis.missing_good_to_have.length > 0) {
        analysis.missing_good_to_have.forEach(skill => {
            missingGoodSkillsDiv.appendChild(createSkill(skill, "missing-good"));
        });
    } else {
        missingGoodSkillsDiv.innerHTML = "<span style='color: #64748b; font-size: 0.9rem;'>None missing.</span>";
    }
}

function createSkill(text, type) {
    const span = document.createElement("span");
    span.className = `skill ${type}`;
    span.textContent = text;
    return span;
}

function resetUI() {
    atsProgressBar.style.width = "0%";
    atsProgressBar.textContent = "0%";
    
    semanticProgressBar.style.width = "0%";
    semanticProgressBar.textContent = "0%";
    
    matchedSkillsDiv.innerHTML = "";
    missingRequiredSkillsDiv.innerHTML = "";
    missingGoodSkillsDiv.innerHTML = "";
    
    suggestionsBox.classList.add("hidden");
    suggestionsText.textContent = "";

    uploadStatus.style.color = "#64748b";
}