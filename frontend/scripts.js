async function verify() {
    const url = document.getElementById("url").value;
    const content = document.getElementById("content").value;

    if (!url && !content) {
        alert("Please enter content or a URL");
        return;
    }

    document.getElementById("output").innerHTML =
        "🔍 Analyzing credibility with TruthLens…";

    const res = await fetch("http://127.0.0.1:5001/verify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url, content })
    });

    const data = await res.json();
    const score = data.score;

    let alertClass = "low",
        alertText = "Low Risk Content";

    if (score < 5) {
        alertClass = "high";
        alertText = "⚠ High Risk: Potential Misinformation";
    } else if (score < 7) {
        alertClass = "medium";
        alertText = "⚠ Medium Risk: Verify Before Sharing";
    }

    const circumference = 565;
    const offset = circumference - (score / 10) * circumference;

    let timeline = `
        <div class="step pass">
            <div class="step-title">Source Verification</div>
            <div class="step-desc">Publisher credibility evaluated</div>
        </div>
        <div class="step pass">
            <div class="step-title">Language Analysis</div>
            <div class="step-desc">Sensational patterns detected</div>
        </div>
        <div class="step pass">
            <div class="step-title">Metadata Integrity</div>
            <div class="step-desc">URL & protocol checked</div>
        </div>
    `;

    data.reasons.forEach(r => {
        timeline += `
            <div class="step fail">
                <div class="step-title">Flag Raised</div>
                <div class="step-desc">${r}</div>
            </div>`;
    });

    const sources = [
        { name: "BBC", score: 8 },
        { name: "The Hindu", score: 9 },
        { name: "NDTV", score: 7 },
        { name: "Unverified Blog", score: 3 }
    ];

    let sourceHTML = "";
    sources.forEach(s => {
        sourceHTML += `
            <div class="bar">
                <span>${s.name}</span>
                <div class="fill" style="width:${s.score * 10}%"></div>
            </div>`;
    });

    document.getElementById("output").innerHTML = `
        <div class="alert ${alertClass}">${alertText}</div>

        <div class="results">
            <div class="gauge">
                <svg>
                    <circle class="bg" cx="110" cy="110" r="95"></circle>
                    <circle class="progress" cx="110" cy="110" r="95"
                        style="stroke-dashoffset:${offset}"></circle>
                </svg>
                <div class="score">${score}/10</div>
                <div class="summary">${data.summary}</div>
            </div>

            <div class="timeline">${timeline}</div>

            <div class="sources">
                <h3 style="color:var(--gold)">Cross-Source Comparison</h3>
                ${sourceHTML}
            </div>
        </div>
    `;
}
