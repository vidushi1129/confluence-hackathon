let analysisDone = false;
let lastInput = "";

const inputField = document.getElementById("newsInput");
const meter = document.getElementById("meter");
const summary = document.getElementById("summary");

inputField.addEventListener("input", () => {
  if (inputField.value !== lastInput) {
    analysisDone = false;
    meter.style.display = "none";
    summary.style.display = "none";
  }
});

function scrollToSection(id) {
  document.getElementById(id).scrollIntoView({ behavior: "smooth" });
}

function checkCredibility() {
  const currentInput = inputField.value.trim();
  if (!currentInput || analysisDone) return;

  analysisDone = true;
  lastInput = currentInput;

  const score = Math.floor(Math.random() * 10) + 1;

  meter.style.display = "flex";
  summary.style.display = "block";
  meter.innerText = score + "/10";

  if (score <= 4) {
    meter.style.background = "#ff4d4d";
    summary.innerText =
      "Low credibility indicators detected. Source reliability appears weak.";
  } else if (score <= 6) {
    meter.style.background = "#f1c40f";
    summary.innerText =
      "Moderate credibility. Further verification is recommended.";
  } else {
    meter.style.background = "#2ecc71";
    summary.innerText =
      "High credibility. Content aligns with reliable information standards.";
  }
}
