# Auto-Icon Supreme

Auto-Icon Supreme is a sophisticated toolset designed for developers and content creators, leveraging the power of FastText embeddings and cosine similarity to semantically match paragraphs of text with the most relevant icons. Whether for enhancing UI/UX design with intuitive iconography or automating the association of concepts with visual symbols, Auto-Icon Supreme streamlines the process, making it both efficient and effective.

## Getting Started

These instructions will guide you through setting up Auto-Icon Supreme on your local machine for development, testing, and deployment purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or newer (I used 3.11)
- pip, Python's package installer

For a smoother experience, familiarity with virtual environments in Python is beneficial but not mandatory.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/timsamart/auto-icon-supreme.git
   ```
   
2. **Navigate to the Project Directory:**
   ```bash
   cd auto-icon-supreme
   ```

3. **(Optional) Set up a Virtual Environment:**
   - For Unix/macOS:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```
   - For Windows:
     ```bash
     py -m venv env
     .\env\Scripts\activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

This sets up your environment with all the dependencies required to run Auto-Icon Supreme.

## Usage

Auto-Icon Supreme is versatile, with scripts supporting various functionalities from embedding generation to finding the best icon matches for your text.

### Basic Usage

- **Generating Icon Embeddings:**
  Use `create_embeddings.py` to generate embeddings for icons based on descriptions provided in a CSV file. This script reads the CSV, processes each icon description through FastText, and saves the generated embeddings for later use.
  ```bash
  python create_embeddings.py
  ```
- **Finding Missing Icons:**
  The `find_missing_icons.py` script compares icons listed in a text file against those in your CSV file, identifying any missing entries.
  ```bash
  python find_missing_icons.py
  ```
- **Matching Text to Icons:**
  With `app.py`, you can match paragraphs of text to the most semantically relevant icons. This script demonstrates the core functionality of Auto-Icon Supreme, utilizing pre-generated embeddings to find the best icon matches for given text inputs.
  ```bash
  python app.py
  ```

### Output
The output for the sample paragraphs:

```python
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
```

**OUTPUT:**

```bash
Execution time: 0.0030 seconds
Execution time: 0.0020 seconds
Execution time: 0.0033 seconds
Execution time: 0.0020 seconds
Execution time: 0.0030 seconds
Execution time: 0.0020 seconds
Execution time: 0.0030 seconds
Execution time: 0.0065 seconds
Execution time: 0.0020 seconds
Execution time: 0.0020 seconds
Execution time: 0.0025 seconds
Execution time: 0.0030 seconds

Paragraph 1:
  sort-amount-desc: 0.6336
  chain: 0.6263
  sort-amount-asc: 0.6257
  eye: 0.6179
  info: 0.5964

Paragraph 2:
  calendar: 0.6018
  chain: 0.6001
  cogs: 0.5875
  institution: 0.5724
  puzzle-piece: 0.5660

Paragraph 3:
  calendar: 0.6075
  calendar-check-o: 0.5444
  check-square-o: 0.5416
  check-square: 0.5416
  toggle-on: 0.5404

Paragraph 4:
  calendar: 0.6393
  check-circle-o: 0.6327
  check-circle: 0.6079
  puzzle-piece: 0.5939
  check-square-o: 0.5911

Paragraph 5:
  calendar: 0.6745
  check-circle-o: 0.6627
  check-circle: 0.6534
  check-square-o: 0.6466
  check-square: 0.6466

Paragraph 6:
  chain: 0.6201
  calendar: 0.6165
  chain-broken: 0.5925
  check-circle-o: 0.5872
  ellipsis-v: 0.5718

Paragraph 7:
  industry: 0.6468
  calendar-plus-o: 0.6389
  question-circle-o: 0.6377
  calendar: 0.6290
  chain: 0.6248

Paragraph 8:
  cart-plus: 0.7088
  calendar-plus-o: 0.6941
  cog: 0.6668
  calendar: 0.6652
  edit: 0.6463

Paragraph 9:
  check-circle-o: 0.6832
  check-circle: 0.6789
  check-square: 0.6505
  check-square-o: 0.6505
  check: 0.6501

Paragraph 10:
  check-circle-o: 0.6254
  question-circle-o: 0.6119
  institution: 0.6108
  check-circle: 0.6037
  chain: 0.6024

Paragraph 11:
  calendar: 0.7168
  calendar-check-o: 0.6607
  check-square-o: 0.6580
  check-square: 0.6580
  check-circle-o: 0.6488

Paragraph 12:
  free-code-camp: 0.6695
  question-circle-o: 0.6348
  institution: 0.6330
  briefcase: 0.6223
  universal-access: 0.6216

Total Execution Time: 0.05 seconds
```

### Advanced Features

For those looking to dive deeper, Auto-Icon Supreme offers advanced customization and functionality:

- **Custom Paragraph Inputs:**
  Modify `app.py` to include your own paragraphs for icon matching. This allows for dynamic matching based on user input or specific content needs.

- **Embedding Customization:**
  Through `create_embeddings.py`, adjust the CSV path or tweak the embedding process to cater to different languages or icon sets. This flexibility ensures that Auto-Icon Supreme can be adapted to a wide range of applications and requirements.

### Folder Structure

Understanding the organization of Auto-Icon Supreme’s files and directories is crucial for navigating and utilizing the project effectively:

```
Auto-Icon Supreme
│
├── env/                         # Virtual environment directory (optional)
│
├── .gitignore                   # Specifies intentionally untracked files to ignore
├── app.py                       # Main application script for matching icons
├── cc.en.300.bin                # Pre-trained FastText model file
├── cc.en.300.bin.gz             # Compressed FastText model file
├── create_embeddings.py         # Script to generate embeddings from CSV
├── falist.txt                   # List of FontAwesome icons
├── fontawesomeassoc.csv         # FontAwesome associations (example)
├── icon_associations*.csv       # Various CSV files with icon associations
├── icon_embeddings.npy          # Numpy file storing the generated embeddings
├── LICENSE                      # The license file
├── README.md                    # README file for the project
├── requirements.txt             # Python dependencies required for the project
└── find_missing_icons_in_dataset.py # Script to find missing icons in dataset
```

### Scripts Explanation

Here's a brief overview of the key scripts included in Auto-Icon Supreme and their functionality:

- **`create_embeddings.py`**: This script takes a CSV file as input, where each row corresponds to an icon and its associated words or phrases. It generates embeddings for these associations using FastText and saves them in a `.npy` file for quick access during the matching process.

- **`find_missing_icons.py`**: A utility script that helps in ensuring the integrity of your icon dataset. It compares the list of icons in `falist.txt` against those present in the `icon_associations.csv`, identifying any icons that may be missing from your dataset.

- **`generate_dataset.py`**: (Placeholder description based on the provided context; adjust as necessary) A script designed to facilitate the expansion of your icon association dataset by automatically generating associated words for each icon through an API call to a language model.

- **`app.py`**: The core script of Auto-Icon Supreme, which allows users to match text paragraphs to the most relevant icons based on semantic similarity. This script showcases the practical application of the embeddings generated by `create_embeddings.py`, using cosine similarity to find and rank the best icon matches for given text inputs.

## Advanced Usage

Beyond basic functionality, Auto-Icon Supreme supports several advanced features that enhance its utility and adaptability:

- **Custom Embeddings**: Users can generate embeddings for new icon sets or update existing ones by modifying the input CSV file used by `create_embeddings.py`. This allows for continuous improvement and expansion of the icon matching capabilities as new icons are added or descriptions are refined.

- **Batch Processing**: For efficiency, `app.py` can be extended to process batches of text inputs, leveraging vectorized operations for faster execution. This is particularly useful for applications that require matching large volumes of text to icons in real-time.

## Contributing

We warmly welcome contributions from the community! If you have an idea for improving Auto-Icon Supreme, or if you've found a bug and know how to fix it, following these steps can help you contribute:

1. **Fork the Repository**: Start by forking the Auto-Icon Supreme repository to your GitHub account.

2. **Create a Feature Branch**: Make a new branch for your feature or bugfix. Naming it something descriptive helps keep things organized.
   ```bash
   git checkout -b feature/YourFeatureName
   ```
   
3. **Commit Your Changes**: Once you're happy with your changes, commit them with a clear, descriptive message. This helps others understand what you've done and why.
   ```bash
   git commit -m 'Add some amazing feature'
   ```

4. **Push to the Branch**: Push your changes up to GitHub.
   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Submit a Pull Request**: Go to the Auto-Icon Supreme repository on GitHub and submit a pull request so your changes can be reviewed.

Feedback, whether in the form of new features, bug reports, or additional documentation, is always appreciated and helps make Auto-Icon Supreme better for everyone.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. The MIT License is a permissive license that is short and to the point. It lets people do anything they want with your code as long as they provide attribution back to you and don’t hold you liable.

## Contact

Should you have any questions, suggestions, or would like to contribute to the project, please feel free to reach out:

- **Project Owner**: [Your Name](timmy@timosam.com)
- **GitHub Repository**: [https://github.com/timsamart/auto-icon-supreme](https://github.com/timsamart/auto-icon-supreme)

## Acknowledgments

- Special thanks to the FastText team for providing the powerful text representation and classification library.
- Gratitude to FontAwesome for their comprehensive and widely used icon set.
- Appreciation for all contributors and users of the Auto-Icon Supreme project, whose feedback and usage help drive continuous improvement.

Thank you for your interest in Auto-Icon Supreme. Whether you're looking to contribute or simply use the project for your needs, we hope it serves you well and enhances your projects with meaningful iconography.

## Troubleshooting Installation Issues

### Compiling FastText on Windows

Users attempting to compile FastText on Windows systems may encounter various challenges, often due to the complexities of setting up a compatible C++ development environment. A key requirement for compiling many C++ projects, including those necessitating Python C extensions, is the Microsoft Visual C++ Redistributable. Without this, or when facing version incompatibilities, missing compilers, or misconfigured environments, users can run into errors that halt the installation process.

### Simplified Installation via Pre-compiled Wheel

To avoid the hurdles associated with compiling from source, we recommend a more straightforward solution: **installing FastText directly using a pre-compiled wheel**. Wheels are binary package formats that contain all necessary components, pre-compiled and packaged, ready for installation. This method negates the need for local compilation, offering a seamless setup experience.

#### Advantages of Using Wheels:

- **Ease of Use**: Directly installing FastText through a wheel file circumvents common pitfalls related to compiling native extensions, offering a user-friendly installation process.
- **Time-Saving**: Eliminates the time and effort required to set up a C++ development environment on Windows systems.
- **Accessibility**: Lowers the barrier to entry for utilizing FastText, making advanced text processing and machine learning functionalities readily available to a broader audience.

### How to Install FastText Using a Wheel

1. Ensure you have Python and `pip` installed on your system.
2. Run the following command in your terminal or command prompt:

   ```bash
   pip install fasttext
   ```

   This command attempts to download and install the latest FastText wheel compatible with your system and Python version.

3. Verify the installation by running:

   ```bash
   python -c "import fasttext; print(fasttext.__version__)"
   ```

If you encounter any issues during the wheel installation or have specific requirements, please consult the [FastText PyPI page](https://pypi.org/project/fasttext/) for additional options and information.

### FastText Model Download

Upon first use of FastText, it's important to note that the library will automatically download a pre-trained model if it's not already present on your system. This is a crucial step for enabling FastText's powerful text processing capabilities.

#### Key Points About the Model Download:

- **Size**: The default model that FastText attempts to download is approximately 1.5 GB in size. Ensure you have sufficient internet bandwidth and storage space.
- **Automatic Download**: This process is automated and occurs the first time you utilize FastText's features that require the pre-trained model.
- **Custom Models**: While the automatic download focuses on a general-purpose model, FastText supports the use of custom models tailored to specific languages or domains. These can be manually downloaded and specified within your application.

### Managing the Model Download

To facilitate a smooth setup, consider the following tips:

1. **Stable Internet Connection**: Ensure a reliable and speedy internet connection before initiating the download to avoid interruptions.
2. **Disk Space**: Verify that you have at least 2 GB of free disk space to accommodate the model without impacting system performance.
3. **Custom Model Usage**: If you prefer to use a custom model or one specific to a different language, you can download it directly from FastText's [official repository](https://fasttext.cc/docs/en/crawl-vectors.html) and load it manually in your application.

#### Example of Manually Loading a Model:

```python
import fasttext

# Replace 'custom_model.bin' with the path to your custom or specifically downloaded model
model = fasttext.load_model('custom_model.bin')
```

By keeping these considerations in mind, you can ensure that your first experience with FastText is as seamless and productive as possible.