import fasttext
import fasttext.util
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re
import time

# Define a simple stop words list; consider using nltk.corpus.stopwords for a comprehensive list
stop_words = set(["the", "and", "a", "an", "in", "on", "at", "for", "with", "without", "to", "of", "by", "as", "is", "are", "was", "were", "be", "being", "been"])

def preprocess_text(text):
    """Convert text to lowercase, remove punctuation, and split into words, excluding stop words."""
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    words = [word for word in words if word not in stop_words]
    return words

# Load FastText's pre-trained model (smaller dimension for efficiency)
fasttext.util.download_model('en', if_exists='ignore')  # English
ft_model = fasttext.load_model('cc.en.300.bin')

def embed_words_fasttext(words, model):
    """Generate embeddings for a list of words using FastText."""
    embeddings = [model.get_word_vector(word) for word in words]
    return np.mean(embeddings, axis=0) if embeddings else np.zeros(model.get_dimension())

# Function to find the best matching icon for given keywords
def find_best_matching_icon(keywords, icon_embeddings, model):
    keyword_embedding = embed_words_fasttext(keywords, model).reshape(1, -1)  # Ensure keyword embedding is 2D
    similarity_scores = {}
    for icon, embedding in icon_embeddings.items():
        # Ensure each icon embedding is also reshaped to 2D
        embedding_2d = embedding.reshape(1, -1)
        similarity = cosine_similarity(keyword_embedding, embedding_2d)[0][0]
        similarity_scores[icon] = similarity

    best_match = max(similarity_scores, key=similarity_scores.get)
    return best_match, similarity_scores[best_match]


def find_best_matching_icons(keywords, icon_embeddings, model, top_n=5):
    start_time = time.time()
    
    # Ensure keyword embedding is reshaped to 2D for similarity computation
    keyword_embedding = embed_words_fasttext(keywords, model).reshape(1, -1)
    
    # Stack all icon embeddings into a single 2D array for vectorized computation
    icons = list(icon_embeddings.keys())
    embeddings = np.array([icon_embeddings[icon] for icon in icons])
    
    # Compute cosine similarities in a vectorized manner
    similarities = cosine_similarity(keyword_embedding, embeddings).flatten()
    
    # Get the indices of the top N matches
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    
    # Prepare the top matches with their scores
    top_matches = [(icons[i], similarities[i]) for i in top_indices]
    
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")
    
    return top_matches


def find_best_matching_icons_for_paragraphs(paragraphs, icon_embeddings, model, top_n=5):
    results = {}
    for idx, paragraph in enumerate(paragraphs):
        # Preprocess and embed the paragraph
        processed_text = preprocess_text(paragraph)
        paragraph_embedding = embed_words_fasttext(processed_text, model).reshape(1, -1)
        
        # Find the best matching icons for this paragraph
        top_matches = find_best_matching_icons(processed_text, icon_embeddings, model, top_n)
        results[f"Paragraph {idx+1}"] = top_matches
    
    return results

def assign_icons_based_on_closest_match(paragraph_matches):
    assigned_icons = {}
    icon_votes = {}

    # Step 1: Collect votes for each icon based on their distance (similarity)
    for paragraph_id, matches in paragraph_matches.items():
        for icon, similarity in matches:
            if icon not in icon_votes:
                icon_votes[icon] = []
            icon_votes[icon].append((paragraph_id, similarity))
    
    # Step 2: Sort votes for each icon by similarity, highest first
    for icon in icon_votes:
        icon_votes[icon].sort(key=lambda x: x[1], reverse=True)
    
    # Step 3: Assign icons to paragraphs based on the closest match
    while icon_votes:
        for icon in list(icon_votes.keys()):  # Iterate over a static list of keys
            if icon not in icon_votes:  # Check if the icon still exists
                continue  # If not, skip to the next icon
            votes = icon_votes[icon]
            top_vote = votes[0]
            paragraph_id = top_vote[0]
            if paragraph_id not in assigned_icons:
                assigned_icons[paragraph_id] = icon
                del icon_votes[icon]  # Safely remove the icon
            else:
                votes.pop(0)  # Remove the top vote and reconsider in the next iteration
                if not votes:
                    del icon_votes[icon]  # Safely remove the icon if no more votes


    # Step 4: Prepare final results
    final_results = {pid: [] for pid in paragraph_matches.keys()}
    for paragraph_id, icon in assigned_icons.items():
        final_results[paragraph_id].append((icon, next((s for i, s in paragraph_matches[paragraph_id] if i == icon), None)))

    return final_results

# Example usage
if __name__ == "__main__":
    user_input = "A discussion on the future of technology and innovation in software development."
    processed_input = preprocess_text(user_input)

    # Load the saved embeddings
    icon_embeddings = np.load("icon_embeddings.npy", allow_pickle=True).item()

    paragraphs = [
        "Enterprise architecture is about understanding the value chain and how individual activities lead to value for the business.",
        "Understanding the business model, distribution channels, and operations is crucial for building flexible IT architecture.",
        "The reporting line of the CIO can indicate the organization's view on the role of IT - as a cost center or a strategic enabler.",
        "Aligning IT Strategy and Business Strategy. Aligning IT strategy with business strategy is key, but the strategy must be translated into reality.",
        "Classifying the business operation model can help determine the appropriate IT strategy, such as containerization.",
        "Understanding the current state of IT systems, often characterized by silos and lack of flexibility, is necessary for defining the target architecture.",
        "Designing Flexible Architecture. Applications often lack flexibility to serve local market needs, which could be a source of business value.",
        "Designing for flexibility, such as through a modular, scalable infrastructure, can unlock new opportunities for the business.",
        "Understanding the value of options and flexibility can help justify investments in architecture, even if the immediate benefits are not obvious.",
        "Governance is essential to ensure that the reality matches the architectural roadmap.",
        "Feedback and adjustment cycles are crucial, as enterprise architecture is not a one-time exercise.",
        "Mentoring and coaching the organization on architectural concepts is important for successful implementation."
    ]

    # Measure execution time for finding matches
    start_time = time.time()

    # Find best matches for paragraphs
    paragraph_matches = find_best_matching_icons_for_paragraphs(paragraphs, icon_embeddings, ft_model, top_n=5)

    # Assign icons based on the closest matches
    final_assignments = assign_icons_based_on_closest_match(paragraph_matches)

    # Display the final assignments
    for paragraph, icons in final_assignments.items():
        print(f"\n{paragraph}:")
        for icon, score in icons:
            print(f"  {icon}: {score:.4f}")

    end_time = time.time()
    print(f"\nTotal Execution Time: {end_time - start_time:.2f} seconds")
