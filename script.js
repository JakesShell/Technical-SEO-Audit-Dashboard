const analyzeBtn = document.getElementById("analyzeBtn");
const urlInput = document.getElementById("url");
const resultsDiv = document.getElementById("results");

function scoreClass(score) {
  if (score >= 90) return "good";
  if (score >= 70) return "medium";
  return "poor";
}

function renderResults(data) {
  const modeBadge = data.mode === "live"
    ? `<span class="badge live">Live API Data</span>`
    : `<span class="badge demo">Demo Mode</span>`;

  const recommendationItems = data.recommendations
    .map(item => `<li>${item}</li>`)
    .join("");

  resultsDiv.innerHTML = `
    <div class="results-header">
      <h2>Audit Results</h2>
      ${modeBadge}
    </div>
    <p><strong>Analyzed URL:</strong> ${data.analyzedUrl}</p>
    ${data.message ? `<p class="info-message">${data.message}</p>` : ""}

    <div class="score-grid">
      <div class="score-card ${scoreClass(data.performance)}">
        <h3>Performance</h3>
        <p>${data.performance}</p>
      </div>
      <div class="score-card ${scoreClass(data.seo)}">
        <h3>SEO</h3>
        <p>${data.seo}</p>
      </div>
      <div class="score-card ${scoreClass(data.accessibility)}">
        <h3>Accessibility</h3>
        <p>${data.accessibility}</p>
      </div>
      <div class="score-card ${scoreClass(data.bestPractices)}">
        <h3>Best Practices</h3>
        <p>${data.bestPractices}</p>
      </div>
    </div>

    <div class="recommendations">
      <h3>Recommended Actions</h3>
      <ul>${recommendationItems}</ul>
    </div>
  `;
}

analyzeBtn.addEventListener("click", async () => {
  const url = urlInput.value.trim();

  if (!url) {
    resultsDiv.innerHTML = `<p class="error-message">Please enter a website URL first.</p>`;
    return;
  }

  resultsDiv.innerHTML = `<p class="loading-message">Analyzing website...</p>`;

  try {
    const response = await fetch("/api/audit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ url })
    });

    const data = await response.json();

    if (!response.ok) {
      resultsDiv.innerHTML = `<p class="error-message">Error: ${data.error}</p>`;
      return;
    }

    renderResults(data);
  } catch (error) {
    resultsDiv.innerHTML = `<p class="error-message">Error: Unable to connect to the server.</p>`;
  }
});
