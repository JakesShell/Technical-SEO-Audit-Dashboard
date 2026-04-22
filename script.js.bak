// public/script.js
document.getElementById('analyzeBtn').addEventListener('click', async () => {
    const url = document.getElementById('url').value;
    const response = await fetch('/api/audit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
    });

    const data = await response.json();
    const resultsDiv = document.getElementById('results');

    if (response.ok) {
        resultsDiv.innerHTML = `
            <h2>Audit Results</h2>
            <p>Page Speed: ${data.speed}%</p>
            <p>Mobile Friendly Score: ${data.mobileFriendly}%</p>
            <!-- Add more metrics as needed -->
        `;
    } else {
        resultsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
    }
});
