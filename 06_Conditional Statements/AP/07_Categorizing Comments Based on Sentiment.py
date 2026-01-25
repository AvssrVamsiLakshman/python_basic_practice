"""
✅ Task Objective:
Accept a user's comment or message as input.
Normalize the input using .strip() and .lower().
Use membership operators to check for specific keywords (e.g., "excellent", "bad", "average", "worst", "great").
Based on these keywords:
• Classify the comment as Positive, Neutral, or Negative.
• Use conditional logic with string comparisons and in/not in to determine the sentiment category.
• Display a categorized summary using f-strings and a decorative line created with repetition.
• Format the summary using newlines (\n) and escape sequences to keep it readable.

🛠 Instructions:
• Prompt the user to input a general text comment.
• Remove extra spaces and convert the text to lowercase for analysis.
• Use in or not in to check if certain sentiment keywords exist in the message.
• Based on the presence of words like:
  - "excellent", "great", "good" → classify as Positive
  - "bad", "worst", "poor" → classify as Negative
  - Otherwise, classify as Neutral
• Print the original comment, the category assigned, and a thank-you note with a divider line above and below.

📤 Sample Output:

Enter your comment: This app is excellent and easy to use!

========================================
Original Comment:
This app is excellent and easy to use!

Sentiment Category: Positive

Thank you for your feedback!
========================================
"""

print("=" * 80)
print("SENTIMENT ANALYSIS PROGRAM")
print("=" * 80)

# Step 1: Prompt user to input a comment
print("\n")
user_comment = input("Enter your comment: ")

# Step 2: Normalize the input
normalized_comment = user_comment.strip().lower()

# Step 3: Define sentiment keywords
positive_keywords = ["excellent", "great", "good", "amazing", "wonderful", 
                     "fantastic", "awesome", "love", "perfect", "best"]

negative_keywords = ["bad", "worst", "poor", "terrible", "awful", 
                     "horrible", "hate", "disappointing", "useless"]

neutral_keywords = ["average", "okay", "fine", "decent", "moderate"]

# Step 4: Check for keywords and classify sentiment
sentiment_category = "Neutral"  # Default

# Check for positive keywords
for keyword in positive_keywords:
    if keyword in normalized_comment:
        sentiment_category = "Positive"
        break

# Check for negative keywords (override if found)
for keyword in negative_keywords:
    if keyword in normalized_comment:
        sentiment_category = "Negative"
        break

# If still neutral, check neutral keywords
if sentiment_category == "Neutral":
    for keyword in neutral_keywords:
        if keyword in normalized_comment:
            sentiment_category = "Neutral"
            break

# Step 5: Display the result
print("\n" + "=" * 40)
print("Original Comment:")
print(user_comment)
print(f"\nSentiment Category: {sentiment_category}")
print("\nThank you for your feedback!")
print("=" * 40)


# Additional demonstrations
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Test comments
test_comments = [
    "This app is excellent and easy to use!",
    "The service was terrible and disappointing.",
    "It's just okay, nothing special.",
    "I love this product! It's amazing!",
    "Worst experience ever. Very bad quality.",
    "The food was decent and the price was average.",
    "Absolutely fantastic! Great job!",
    "Poor quality and awful customer service."
]

print("\nAnalyzing sample comments:")

for comment in test_comments:
    # Normalize
    norm = comment.lower()
    
    # Classify
    category = "Neutral"
    
    # Check positive
    for kw in positive_keywords:
        if kw in norm:
            category = "Positive"
            break
    
    # Check negative (override)
    for kw in negative_keywords:
        if kw in norm:
            category = "Negative"
            break
    
    print(f"\n  Comment: {comment}")
    print(f"  Sentiment: {category}")


# Enhanced sentiment analysis
print("\n" + "=" * 80)
print("BONUS: Enhanced Sentiment Analysis with Scoring")
print("=" * 80)

def analyze_sentiment_score(text):
    """
    Analyze sentiment with a numeric score
    Returns: (category, score, keywords_found)
    """
    normalized = text.lower()
    
    positive_words = ["excellent", "great", "good", "amazing", "wonderful", 
                      "fantastic", "awesome", "love", "perfect", "best"]
    
    negative_words = ["bad", "worst", "poor", "terrible", "awful", 
                      "horrible", "hate", "disappointing", "useless"]
    
    # Count keywords
    pos_count = sum(1 for word in positive_words if word in normalized)
    neg_count = sum(1 for word in negative_words if word in normalized)
    
    # Calculate score
    score = pos_count - neg_count
    
    # Determine category
    if score > 0:
        category = "Positive"
    elif score < 0:
        category = "Negative"
    else:
        category = "Neutral"
    
    # Find keywords
    found_positive = [word for word in positive_words if word in normalized]
    found_negative = [word for word in negative_words if word in normalized]
    
    return category, score, found_positive, found_negative

# Test enhanced analysis
enhanced_comment = input("\nEnter comment for enhanced analysis: ")
category, score, pos_words, neg_words = analyze_sentiment_score(enhanced_comment)

print("\n" + "-" * 40)
print(f"Comment: {enhanced_comment}")
print(f"Sentiment: {category}")
print(f"Score: {score:+d}")

if pos_words:
    print(f"Positive words found: {', '.join(pos_words)}")
if neg_words:
    print(f"Negative words found: {', '.join(neg_words)}")
print("-" * 40)


# Emoji addition based on sentiment
print("\n" + "=" * 80)
print("BONUS: Sentiment with Emoji Response")
print("=" * 80)

sentiment_emojis = {
    "Positive": "😊 👍 ⭐",
    "Negative": "😞 👎 ⚠️",
    "Neutral": "😐 ➖"
}

emoji_comment = input("\nEnter your comment: ")
emoji_norm = emoji_comment.lower()

# Classify
emoji_sentiment = "Neutral"

for kw in positive_keywords:
    if kw in emoji_norm:
        emoji_sentiment = "Positive"
        break

for kw in negative_keywords:
    if kw in emoji_norm:
        emoji_sentiment = "Negative"
        break

print("\n" + "=" * 40)
print(f"Sentiment: {emoji_sentiment} {sentiment_emojis[emoji_sentiment]}")
print("=" * 40)


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
