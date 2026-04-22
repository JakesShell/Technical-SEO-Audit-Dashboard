# Technical SEO Audit Dashboard

## Overview

Technical SEO Audit Dashboard is a Node.js and Express web application that analyzes a target website and returns a simplified audit view focused on technical SEO and related quality signals.

The dashboard is designed as a portfolio-ready business tool for digital marketers, SEO specialists, web consultants, and agencies who need a fast way to review a site's health from a performance and optimization perspective.

This project supports two operating modes:

- **Live mode**, when a valid Google PageSpeed API key is configured
- **Demo mode**, when no API key is present

That means the application remains fully usable as a recruiter demo even without external API setup.

## Real-World Business Use Case

This project maps to a realistic agency or in-house marketing workflow.

A business may need to answer questions such as:

- Is this website fast enough for a good user experience?
- Are there technical signals that may hurt SEO performance?
- Is the site reasonably accessible?
- Are best practices being followed?
- What actions should the team take first?

This type of tool could be used by:

- freelance SEO consultants
- digital marketing agencies
- website performance auditors
- in-house growth teams
- web development teams reviewing client sites

## Key Features

- URL input for target website analysis
- Server-side audit endpoint using Node.js and Express
- Demo mode fallback when no API key is configured
- Support for live API-based audit mode
- Dashboard cards for:
  - Performance
  - SEO
  - Accessibility
  - Best Practices
- Recommended action list for follow-up improvements
- Responsive browser-based interface

## Tech Stack

- Node.js
- Express
- JavaScript
- HTML
- CSS
- Axios
- CORS

## Project Structure

```text
Technical-SEO-Audit-Dashboard/
|-- index.html
|-- styles.css
|-- script.js
|-- server.js
|-- package.json
|-- package-lock.json
|-- .gitignore
|-- .env.example
|-- README.md
|-- docs/
|   |-- images/
|       |-- seo-dashboard-demo.png
