import os
import glob
import random

# Input folders by genre
genre_folders = {
    "pop": "corpus_pop",
    "rap": "corpus_rap",
    "rnb": "corpus_rnb"
}

# Output base folder
output_base = "corpus_increase1"
os.makedirs(output_base, exist_ok=True)

def extract_random_lines(text, n=4, min_start=2):
    """Extract n random lines from text, starting after min_start lines"""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) <= n + min_start:
        return None  # Skip too short texts
    candidates = lines[min_start:]
    return random.sample(candidates, n) if len(candidates) >= n else None

def generate_synthetic_texts(genre_path, n_files=60, lines_per_text=4):
    """Generate synthetic texts by randomly sampling lines from files"""
    filepaths = glob.glob(os.path.join(genre_path, "*.txt"))
    excerpts = []

    for path in filepaths:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        sampled = extract_random_lines(text, n=lines_per_text)
        if sampled:
            excerpts.append("\n".join(sampled))

    if len(excerpts) < lines_per_text:
        print("Pas assez de données pour ce genre.")
        return

    return excerpts

def build_files_from_excerpts(excerpts, out_dir, n_files=60, lines_per_text=4, prefix="synthetic_"):
    """Build final .txt files from random selections of excerpts"""
    os.makedirs(out_dir, exist_ok=True)
    count = 0

    while count < n_files:
        selected = random.choices(excerpts, k=lines_per_text)
        text = "\n\n".join(selected)
        filename = os.path.join(out_dir, f"{prefix}{count+1}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        count += 1

# Process each genre
for genre, folder in genre_folders.items():
    print(f"Genre traité : {genre}")
    out_folder = os.path.join(output_base, genre)
    excerpts = generate_synthetic_texts(folder)
    if excerpts:
        build_files_from_excerpts(excerpts, out_folder)
        print(f"- 60 fichiers générés dans {out_folder}")
    else:
        print(f"- Aucune donnée suffisante pour le genre {genre}.")

print("Création du corpus synthétique terminée.")
