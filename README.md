# Hackathon 3.0 – First-Aid AI App

## Overview
This is a beginner-friendly AI-powered First-Aid app built with Flask, MySQL, and a Hugging Face AI API.  
It allows users to input symptoms and receive immediate first-aid advice. If the AI API is unavailable, the app provides a basic offline emergency guide.

## Features
- User inputs symptoms via a simple HTML form.
- AI analyzes symptoms and provides advice.
- Stores user entries in MySQL (Create, Read, Update, Delete functionality).
- Offline emergency guide for common situations.
- Visual feedback for severity of symptoms (optional charts can be added).

## Tech Stack
- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python (Flask)
- **Database:** MySQL
- **AI:** Hugging Face API (Sentiment / text analysis)
- **Environment Variables:** `.env` file for secure API token

## Setup Instructions
1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/hackathon3.0.git
cd hackathon3.0

## How to Test
1. Run `app.py` with Flask.
2. Open your browser at http://127.0.0.1:5000
3. Enter symptoms and click submit to see AI advice or offline guidance.
