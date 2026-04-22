const express = require("express");
const axios = require("axios");
const cors = require("cors");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 5000;
const API_KEY = process.env.PAGESPEED_API_KEY || "";

app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

function normalizeUrl(input) {
  if (!input || typeof input !== "string") return "";
  const trimmed = input.trim();
  if (!trimmed) return "";
  if (/^https?:\/\//i.test(trimmed)) return trimmed;
  return `https://${trimmed}`;
}

function buildDemoResults(targetUrl) {
  return {
    mode: "demo",
    analyzedUrl: targetUrl,
    performance: 84,
    seo: 91,
    accessibility: 88,
    bestPractices: 86,
    recommendations: [
      "Compress and properly size large images.",
      "Add descriptive meta titles and meta descriptions.",
      "Improve internal linking to important pages.",
      "Minify CSS and JavaScript assets.",
      "Review mobile spacing and tap target sizing."
    ]
  };
}

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.post("/api/audit", async (req, res) => {
  const rawUrl = req.body?.url;
  const targetUrl = normalizeUrl(rawUrl);

  if (!targetUrl) {
    return res.status(400).json({ error: "Please enter a valid URL." });
  }

  try {
    new URL(targetUrl);
  } catch {
    return res.status(400).json({ error: "The URL format is invalid." });
  }

  if (!API_KEY) {
    return res.json({
      ...buildDemoResults(targetUrl),
      message: "Running in demo mode because no Google PageSpeed API key is configured."
    });
  }

  try {
    const apiUrl = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed";
    const response = await axios.get(apiUrl, {
      params: {
        url: targetUrl,
        key: API_KEY,
        strategy: "mobile",
        category: ["performance", "seo", "accessibility", "best-practices"]
      }
    });

    const categories = response.data?.lighthouseResult?.categories || {};

    const results = {
      mode: "live",
      analyzedUrl: targetUrl,
      performance: Math.round((categories.performance?.score || 0) * 100),
      seo: Math.round((categories.seo?.score || 0) * 100),
      accessibility: Math.round((categories.accessibility?.score || 0) * 100),
      bestPractices: Math.round((categories["best-practices"]?.score || 0) * 100),
      recommendations: [
        "Review Core Web Vitals and improve slow-loading assets.",
        "Strengthen on-page metadata and heading structure.",
        "Audit mobile usability and page responsiveness.",
        "Reduce render-blocking resources where possible.",
        "Improve caching and asset delivery performance."
      ]
    };

    return res.json(results);
  } catch (error) {
    return res.status(500).json({
      error: "Unable to fetch live audit data. Check the API key or try demo mode."
    });
  }
});

app.listen(PORT, () => {
  console.log(`SEO Audit Dashboard is running on http://localhost:${PORT}`);
});
