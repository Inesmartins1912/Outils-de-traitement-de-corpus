{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b1aeaa55-7e8f-4084-843d-90b5d6291894",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Genre traité : pop\n",
      "- 60 fichiers générés dans corpus_increase1/pop\n",
      "Genre traité : rap\n",
      "- 60 fichiers générés dans corpus_increase1/rap\n",
      "Genre traité : rnb\n",
      "- 60 fichiers générés dans corpus_increase1/rnb\n",
      "Création du corpus synthétique terminée.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import glob\n",
    "import random\n",
    "\n",
    "# Input folders by genre\n",
    "genre_folders = {\n",
    "    \"pop\": \"corpus_pop\",\n",
    "    \"rap\": \"corpus_rap\",\n",
    "    \"rnb\": \"corpus_rnb\"\n",
    "}\n",
    "\n",
    "# Output base folder\n",
    "output_base = \"corpus_increase1\"\n",
    "os.makedirs(output_base, exist_ok=True)\n",
    "\n",
    "def extract_random_lines(text, n=4, min_start=2):\n",
    "    \"\"\"Extract n random lines from text, starting after min_start lines\"\"\"\n",
    "    lines = [line.strip() for line in text.splitlines() if line.strip()]\n",
    "    if len(lines) <= n + min_start:\n",
    "        return None  # Skip too short texts\n",
    "    candidates = lines[min_start:]\n",
    "    return random.sample(candidates, n) if len(candidates) >= n else None\n",
    "\n",
    "def generate_synthetic_texts(genre_path, n_files=60, lines_per_text=4):\n",
    "    \"\"\"Generate synthetic texts by randomly sampling lines from files\"\"\"\n",
    "    filepaths = glob.glob(os.path.join(genre_path, \"*.txt\"))\n",
    "    excerpts = []\n",
    "\n",
    "    for path in filepaths:\n",
    "        with open(path, \"r\", encoding=\"utf-8\") as f:\n",
    "            text = f.read()\n",
    "        sampled = extract_random_lines(text, n=lines_per_text)\n",
    "        if sampled:\n",
    "            excerpts.append(\"\\n\".join(sampled))\n",
    "\n",
    "    if len(excerpts) < lines_per_text:\n",
    "        print(\"Pas assez de données pour ce genre.\")\n",
    "        return\n",
    "\n",
    "    return excerpts\n",
    "\n",
    "def build_files_from_excerpts(excerpts, out_dir, n_files=60, lines_per_text=4, prefix=\"synthetic_\"):\n",
    "    \"\"\"Build final .txt files from random selections of excerpts\"\"\"\n",
    "    os.makedirs(out_dir, exist_ok=True)\n",
    "    count = 0\n",
    "\n",
    "    while count < n_files:\n",
    "        selected = random.choices(excerpts, k=lines_per_text)\n",
    "        text = \"\\n\\n\".join(selected)\n",
    "        filename = os.path.join(out_dir, f\"{prefix}{count+1}.txt\")\n",
    "        with open(filename, \"w\", encoding=\"utf-8\") as f:\n",
    "            f.write(text)\n",
    "        count += 1\n",
    "\n",
    "# Process each genre\n",
    "for genre, folder in genre_folders.items():\n",
    "    print(f\"Genre traité : {genre}\")\n",
    "    out_folder = os.path.join(output_base, genre)\n",
    "    excerpts = generate_synthetic_texts(folder)\n",
    "    if excerpts:\n",
    "        build_files_from_excerpts(excerpts, out_folder)\n",
    "        print(f\"- 60 fichiers générés dans {out_folder}\")\n",
    "    else:\n",
    "        print(f\"- Aucune donnée suffisante pour le genre {genre}.\")\n",
    "\n",
    "print(\"Création du corpus synthétique terminée.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3b1e218-1790-41c9-aa30-60dae8963855",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
