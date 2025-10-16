# Meeting Summarizer

## Overview
Meeting Summarizer is a fullstack AI-powered application designed to transcribe meeting audio and generate concise, action-oriented summaries. It processes meeting audio files to produce accurate transcripts, highlight key decisions, and extract actionable tasks, providing a seamless way to capture and share meeting insights.

## Features
- Upload meeting audio files (MP3, WAV, etc.) via a React frontend  
- Automatic transcription using OpenAI Whisper speech-to-text model  
- Summarization and extraction of key decisions and action items using a local DistilBART model  
- Backend API using Flask for processing and serving data  
- User-friendly interface to view transcripts, summaries, and copy action items

## Tech Stack
- **Frontend:** React (JavaScript, HTML, CSS)  
- **Backend:** Python Flask  
- **Speech-to-Text:** OpenAI Whisper  
- **Summarization:** `sshleifer/distilbart-cnn-12-6` via Hugging Face Transformers (CPU-friendly)  

## Setup Instructions

### Backend
1. Navigate to the backend folder:
   cd backend
2. Activate your Python virtual environment:
- Windows:
  ```
  env\Scripts\activate
  ```
- Mac/Linux:
  ```
  source env/bin/activate
  ```
3. Install dependencies :
 ```
  pip install -r requirements.txt
  ```
4. Run the Flask backend:
  ```
  python app.py
  ```

### Frontend
1. Navigate to the frontend folder:
   ```
   cd frontend
   ```
2. Install Node.js dependencies:
   ```
   npm install
   ```
3. Start the React development server:
   ```
   npm start
   ```
4. Open your browser at `http://localhost:3000` to access the frontend.

## Usage
- Upload your meeting audio through the UI.  
- Wait for transcription and summarization to complete.  
- View generated transcript, key decisions, and action items.  
- Copy summaries and share.

## Project Scope & Evaluation Focus
- Integration with ASR APIs such as OpenAI Whisper for speech transcription  
- Backend storage and processing of data  
- Use of LLMs for generating human-readable, structured summaries  
- Emphasis on transcription accuracy, summary quality, prompt effectiveness, and clean code structure




   
   
   
   

   
   
