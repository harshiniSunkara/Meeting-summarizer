# gpt_utils.py
from transformers import pipeline

def load_summarizer():
    """Load a small summarization model suitable for CPU-only systems."""
    try:
        summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",
            tokenizer="sshleifer/distilbart-cnn-12-6",
            device=-1  # use CPU
        )
        return summarizer
    except Exception as e:
        print("Error loading summarization model:", e)
        return None

summarizer = load_summarizer()

def chunk_text(text, max_chars=3000):
    """Split long text into smaller chunks for safer summarization."""
    chunks = []
    while len(text) > max_chars:
        split_index = text.rfind('.', 0, max_chars)
        if split_index == -1:
            split_index = max_chars
        chunk = text[:split_index + 1]
        chunks.append(chunk)
        text = text[split_index + 1:]
    if text.strip():
        chunks.append(text)
    return chunks

def analyse_meeting(transcript: str) -> dict:
    """
    Prompt for Meeting Transcript Analysis:

    You are a professional AI meeting assistant.  
    Analyze the following meeting transcript and provide a clear, concise, and organized report containing:

    1. A brief summary highlighting the meeting’s purpose and main points (3-5 sentences).  
    2. A list of key decisions made during the meeting, stated clearly and specifically.  
    3. A list of actionable tasks assigned during the meeting, including responsible persons and deadlines if mentioned.

    Structure your response as a JSON object with keys:  
    - "summary": string  
    - "decisions": array of strings  
    - "action_items": array of strings  

    Ensure the language is professional, unambiguous, and suitable for business documentation.

    Transcript:  
    {transcript}
    """

    if not transcript or len(transcript.strip()) == 0:
        return {"error": "Empty transcript provided."}

    try:
        chunks = chunk_text(transcript)
        summaries = []
        for chunk in chunks:
            result = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
            summaries.append(result[0]['summary_text'].strip())

        combined_summary = " ".join(summaries)

        return {
            "summary": combined_summary,
            "decisions": extract_decisions(combined_summary),
            "action_items": extract_actions(combined_summary)
        }
    except Exception as e:
        print("Error analyzing meeting:", e)
        return {"error": str(e)}

def extract_decisions(text: str):
    lines = [line.strip() for line in text.split('.') if any(k in line.lower() for k in ["decided", "approved", "agreed", "confirmed"])]
    return lines or ["No major decisions detected."]

def extract_actions(text: str):
    lines = [line.strip() for line in text.split('.') if any(k in line.lower() for k in ["will", "assigned", "to do", "prepare", "follow up"])]
    return lines or ["No clear action items found."]
