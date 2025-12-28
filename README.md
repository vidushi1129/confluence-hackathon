#🔍 TruthLens — Misinformation Detection & News Credibility Analyzer

“In an era where misinformation spreads faster than facts, TruthLens helps users see the truth clearly.”

#🚀 Project Overview

TruthLens is a web-based news verification and misinformation detection tool designed to evaluate the credibility of news articles in real time.
It combines rule-based analysis, source credibility scoring, language pattern detection, and cross-source comparison to help users make informed decisions before consuming or sharing news.

This project was built to address a real-world problem:
👉 the rapid spread of fake or misleading news across digital platforms.

#❓ Problem Statement

With the exponential growth of online media:

False or misleading news spreads faster than verified facts

Users often lack tools to quickly evaluate credibility

Clickbait headlines and unverified sources create confusion and panic

TruthLens provides a simple yet powerful solution to verify news authenticity instantly.

💡 Key Features
🧠 Credibility Scoring Engine

Generates a credibility score (0–10)

Based on:

Source reliability

Sensational language detection

Metadata and content checks

#🌍 Source Credibility Analysis

Uses a curated list of Indian (North & South) and international news sources

Scores trusted publishers higher

Flags unknown or low-credibility domains

📰 News Scraper (Backend)

Automatically extracts article text from URLs

Allows users to verify news without manual copying

#📊 Animated Credibility Gauge

Visual representation of trust score

Color-coded risk levels:

🟢 Low risk

🟡 Medium risk

🔴 High risk

🧭 Verification Timeline

Step-by-step breakdown of how credibility was assessed

Improves transparency and explainability

⚠ Live Risk Alerts

Instantly warns users when content is suspicious

Encourages responsible sharing

📈 Cross-Source Comparison

Compares credibility across multiple sources

Highlights inconsistencies and bias

🛠️ Tech Stack
Frontend

HTML, CSS, JavaScript

Animated UI components

Responsive & dark-mode design

Backend

Python (Flask)

RESTful API architecture

CORS enabled for frontend integration

Libraries & Tools

newspaper3k – Article scraping

regex – Language pattern analysis

Flask – Backend server

Postman – API testing
##how to run
1.Install dependence: 'pip install -r requirements.txt'
2.Go to backend folder 
3.Run: ' python app.py'
4.API runs at http://127.0.0.1:5001
