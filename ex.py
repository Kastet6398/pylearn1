from faker import Faker
import pyperclip
import random

def generate_chinese_sentences(num_sentences, min_words, max_words):
    fake = Faker('zh_CN')  # Set the locale to Chinese (Simplified)
    sentences = []

    for _ in range(num_sentences):
        num_words = random.randint(min_words, max_words)
        sentence_words = [fake.word() for _ in range(num_words)]
        sentences.append(sentence_words)

    sentences_string = '。'.join([' '.join(sentence) for sentence in sentences])
    return sentences_string

# Generate 20 sentences with a random number of words between 10 and 15
result = generate_chinese_sentences(20, 10, 15)

# Copy the result to the clipboard
pyperclip.copy(result)

# Print a message
print("Generated Chinese sentences with random words copied to clipboard.")

