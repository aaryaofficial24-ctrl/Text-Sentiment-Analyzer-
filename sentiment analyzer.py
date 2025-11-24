import string

# Simple Sentiment Analysis in Python (Rule-Based)
# This program analyzes the sentiment of a given sentence by counting positive and negative word given in the input

# list of good and bad words
POSITIVE_WORDS = [
    # good word bank
    "good", "great", "excellent", "amazing", "wonderful", "fantastic", "love", 
    "like", "happy", "joy", "best", "awesome", "brilliant", "superb", "delightful",
    "adaptable", "benevolent", "brilliant", "capable", "charismatic", 
    "compassionate", "courageous", "dazzling", "diligent", "dynamic", 
    "ebullient", "efficient", "empathetic", "exuberant", "faithful", 
    "fantastic", "flourishing", "generous", "gratitude", "harmonious", 
    "honest", "illuminating", "ingenious", "inspiring", "joyous", 
    "jubilant", "kindhearted", "knowledgeable", "luminous", "magnificent", 
    "motivated", "noble", "optimistic", "outstanding", "passionate", 
    "peaceful", "prosperous", "radiant", "reliable", "resilient", 
    "sincere", "tenacious", "thriving", "trustworthy", "unwavering", 
    "vibrant", "vivacious", "wholesome", "wonderful", "zealous"
]

NEGATIVE_WORDS = [
    # bad word bank
    "bad", "terrible", "awful", "horrible", "hate", "dislike", "sad", "angry", 
    "worst", "ugly", "poor", "disappointing", "boring", "annoying", "frustrating",
    "abrasive", "apathetic", "arrogant", "belligerent", "callous", 
    "chaotic", "cynical", "deceitful", "deficient", "deplorable", 
    "detrimental", "disastrous", "dreadful", "egotistical", "exhausting", 
    "fickle", "fraudulent", "ghastly", "gloomy", "gruesome", 
    "harsh", "hostile", "ignorant", "impatient", "incompetent", 
    "insipid", "irrational", "jealous", "lethargic", "malicious", 
    "mediocre", "menacing", "narcissistic", "nefarious", "neglectful", 
    "obnoxious", "oppressive", "pessimistic", "petty", "prejudiced", 
    "repulsive", "ruthless", "scornful", "spiteful", "tedious", 
    "toxic", "unreliable", "vengeful", "vile", "wasteful"
]

# to tokenize sentiment
def tokenize_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    return words

# analyze sentiment
def analyze_sentiment(text):
    words = tokenize_text(text)
    positive_count = 0
    negative_count = 0
    
    for word in words:
        if word in POSITIVE_WORDS:
            positive_count += 1
        elif word in NEGATIVE_WORDS:
            negative_count += 1
    
    # calculate score
    score = positive_count - negative_count
    
    # calculate sentiment
    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, score, positive_count, negative_count

# Main function
def main():
    print("Simple Sentiment Analysis Tool")
    
    # --- Test Case for Demonstration ---
    test_sentence = "This project is fantastic and brilliant, but the delay was awful and disappointing."
    print(f"\nAnalyzing test sentence: '{test_sentence}'")
    
    sentiment, score, pos_count, neg_count = analyze_sentiment(test_sentence)
    
    print(f"Sentiment: {sentiment}")
    print(f"Score: {score} (Positive words: {pos_count}, Negative words: {neg_count})")
    print("-" * 40)


# to check if script is being run directly
if __name__ == "__main__":
    main()