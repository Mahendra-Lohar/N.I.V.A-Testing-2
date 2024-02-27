
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
from speak import Say
# from Listen import listen
def text_summarization(text, num_sentences=10):
    """
    Summarizes the given text using NLTK's TextRank algorithm.

    Parameters:
        text (str): The input text to be summarized.
        num_sentences (int): The number of sentences in the summary (default is 3).

    Returns:
        summary (str): The summarized text.
    """
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    # Calculate word frequency
    word_freq = FreqDist(words)

    # Assign scores to sentences based on word frequency
    sent_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_freq:
                if len(sentence.split(" ")) < 50:  # Only consider sentences with less than 30 words
                    if sentence not in sent_scores:
                        sent_scores[sentence] = word_freq[word]
                    else:
                        sent_scores[sentence] += word_freq[word]

    # Select top 'num_sentences' sentences with highest scores
    summary_sentences = nlargest(num_sentences, sent_scores, key=sent_scores.get)

    # Join the summary sentences to form the summary
    summary = " ".join(summary_sentences)
    return summary

# Example usage:
Say("Enter the Text for Summarization:")
text=input("Enter the Text for Summarization here:")
input_text = "'''"+text+"''''"

summary = text_summarization(input_text)
Say("Summary for text is below:")
Say(summary)
