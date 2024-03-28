import pandas as pd
import fasttext.util
import numpy as np

# Load FastText model
fasttext.util.download_model('en', if_exists='ignore')  # English
ft_model = fasttext.load_model('cc.en.300.bin')

def embed_words_fasttext(words, model):
    """Generate embeddings for a list of words using FastText."""
    embeddings = [model.get_word_vector(word.strip()) for word in words if word.strip()]
    return np.mean(embeddings, axis=0) if embeddings else np.zeros(model.get_dimension())

def load_csv_and_generate_embeddings(csv_path):
    """Load a CSV file, generate embeddings for each icon's associations, and return a dictionary of embeddings."""
    # Initialize an empty dictionary to store embeddings
    embeddings_dict = {}
    # Open the CSV file
    with open(csv_path, 'r', encoding='utf-8') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into fields using comma as delimiter
            fields = line.strip().split(',')
            if fields:  # Check if line is not empty
                icon_name = fields[0]  # First field is the icon name
                associations = fields[1:]  # The rest are the associations
                embeddings_dict[icon_name] = embed_words_fasttext(associations, ft_model)
    return embeddings_dict


def save_embeddings(embeddings_dict, save_path="icon_embeddings.npy"):
    """Save the generated embeddings dictionary as a NumPy array file."""
    np.save(save_path, embeddings_dict)

# Path to your CSV file
csv_path = "icon_associations_nobrands.csv"  # Update this path

# Generate embeddings
embeddings_dict = load_csv_and_generate_embeddings(csv_path)

# Save embeddings to file
save_embeddings(embeddings_dict)

print(f"Embeddings have been generated and saved to icon_embeddings.npy.")
