from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_transcript(video_id):
    """
    Fetches the transcript of a YouTube video using the video ID.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])
        return text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
# Load Hugging Face sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text using Hugging Face pipeline.
    Splits text into manageable chunks to handle token limits.
    """
    try:
        # Split text into smaller chunks to avoid token length issues
        max_chunk_size = 512
        chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        
        sentiments = []
        for chunk in chunks:
            sentiment = sentiment_analyzer(chunk)
            sentiments.extend(sentiment)

        return sentiments
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return None

def analyze_youtube_video_sentiment(video_id):
    """
    Fetches the transcript of a YouTube video and performs sentiment analysis on it.
    """
    transcript = get_video_transcript(video_id)
    if transcript:
        print("Transcript fetched successfully.")
        sentiments = analyze_sentiment(transcript)
        if sentiments:
            # Aggregate results
            positive = sum(1 for s in sentiments if s['label'] == 'POSITIVE')
            negative = sum(1 for s in sentiments if s['label'] == 'NEGATIVE')
            total = len(sentiments)

            print("Sentiment Analysis Result:")
            print(f"Positive: {positive} ({positive / total * 100:.2f}%)")
            print(f"Negative: {negative} ({negative / total * 100:.2f}%)")
        else:
            print("No sentiment analysis result available.")
    else:
        print("No transcript available for the video.")

# Example usage
if __name__ == "__main__":
    video_id = "vnzltrJSHNc"  # Replace with your YouTube video ID
    analyze_youtube_video_sentiment(video_id)
