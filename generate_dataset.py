import anthropic
import time

# Assuming 'anthroware' or the correct package is already installed and imported
api_key = "placeholder"
client = anthropic.Anthropic(api_key=api_key)

# Load icons from file
icons = []
with open('falist.txt', 'r') as file:
    icons = [line.strip() for line in file.readlines()]
    print(f"Loaded {len(icons)} icons from falist.txt.")

# Splitting the icon list into batches of 30
batch_size = 30
icon_batches = [icons[i:i + batch_size] for i in range(0, len(icons), batch_size)]
total_batches = len(icon_batches)
print(f"Split icons into {total_batches} batches of {batch_size}.")

csv_output_path = 'icon_associations.csv'

systemString="Your job is to add 40 best associated words to the fontawesome icons i will paste you. the output should be a csv with the fontawesome iconname as the first csv value and then the 40 best associated words. The words should include:\n\nDirect Use: Words that describe the icon's literal depiction or primary function.\nSymbolic Representation: Words that represent what the icon symbolizes in different contexts.\nContextual Application: Words associated with the contexts or environments in which the icon might be used.\nRelated Actions: Words that describe actions or processes related to the icon."


for batch_index, batch in enumerate(icon_batches, start=1):
    print(f"\nProcessing batch {batch_index}/{total_batches}...")
    content = "\n".join(batch)
    messages = [{"role": "user", "content": content}]
    
    try:
        start_time = time.time()
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=4000,
            temperature=0,
            system=systemString,
            messages=messages
        )
        end_time = time.time()
        
        # Assuming 'response.content[0].text' contains the CSV content directly
        csv_content = response.content[0].text  # Adjust according to the actual structure
        
        # Append the response to a CSV file
        with open(csv_output_path, 'a', newline='') as f:
            f.write(csv_content + '\n')
        
        print(f"Batch {batch_index} processed and appended to CSV. Time taken: {end_time - start_time:.2f} seconds.")
        
    except Exception as e:
        print(f"An error occurred with batch {batch_index}: {e}")
        
    # Optional: print progress after each batch
    progress_percentage = (batch_index / total_batches) * 100
    print(f"Progress: {progress_percentage:.2f}% completed.")

print("\nAll batches processed and results appended to 'icon_associations.csv'.")

