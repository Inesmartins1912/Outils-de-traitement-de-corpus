import os
import glob
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Chemins des dossiers par genre
genre_folders = {
    "pop": "corpus_pop/*",
    "rap": "corpus_rap/*",
    "rnb": "corpus_rnb/*"
}

# Fonction de lecture des paroles
def read_lyrics(folder_path, genre):
    data = []
    for filepath in glob.glob(os.path.join(folder_path, "*.txt")):
        print(f"Exploring: {os.path.join(folder_path, '*.txt')}")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
                data.append({
                    "Genre": genre,
                    "File": os.path.basename(filepath),
                    "Lyrics": text
                })
        except Exception as e:
            print(f"Erreur de lecture de {filepath} : {e}")
    return data

# Tokenisation simple (sans NLTK)
def simple_tokenize(text):
    tokens = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return tokens

# Collecte des données
corpus = []
for genre, folder in genre_folders.items():
    corpus.extend(read_lyrics(folder, genre))

# Vérification
if not corpus:
    print("Aucune donnée trouvée. Vérifie les chemins des dossiers.")
    exit()

df = pd.DataFrame(corpus)

# Vérification de la colonne Lyrics
if "Lyrics" not in df.columns:
    print("Colonne 'Lyrics' manquante dans le DataFrame.")
    exit()

# Longueur des textes
df["Length"] = df["Lyrics"].apply(lambda t: len(simple_tokenize(str(t))))

# Distribution des longueurs
def plot_text_lengths(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df["Length"], bins=30, kde=True)
    plt.title("Distribution of lyrics length (in words)")
    plt.xlabel("Number of words")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    print("Average length:", df["Length"].mean())
    print("Max length:", df["Length"].max())
    print("Min length:", df["Length"].min())

# Distribution des mots les plus fréquents (loi de Zipf)
def plot_zipf(df, top_n=50):
    all_tokens = []
    for text in df["Lyrics"].dropna():
        tokens = simple_tokenize(text)
        all_tokens.extend(tokens)

    counter = Counter(all_tokens)
    most_common = counter.most_common(top_n)
    if not most_common:
        print("Aucune donnée pour Zipf.")
        return

    words, freqs = zip(*most_common)

    plt.figure(figsize=(14, 6))
    sns.barplot(x=list(words), y=list(freqs))
    plt.title(f"Top {top_n} frequent words")
    plt.xticks(rotation=45)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Exécution
plot_text_lengths(df)
plot_zipf(df)
