# Projet d'Outils de traitement de corpus

**Tâche choisie : Classification de chansons par genre à partir des paroles**

## Description

Ce projet a pour objectif de classifier automatiquement des chansons par genre musical (rap, pop et R&B) sur la base de l'analyse de leurs paroles uniquement. Le modèle ne dispose ainsi ni de la musique ni de métadonnées pouvant lui donner des indices pour la classification : il se base exclusivement sur le contenu lexical des textes.

Pour ce faire il faut dans un premier temps constituer un corpus d'environ 300 chansons en anglais (100 par genre musical pour une question d'équilibre du jeu de données), à l'aide d'un scrip permettant de scraper depuis le web. Puis dans un deuxième temps il faut appliquer au corpus des scripts de prétraitement, vectorisation, analyse exploratoire et classification supervisée à l’aide de la bibliothèque scikit-learn.

---

## Contenu du dépôt :

```
Outils_de_traitement_de_corpus/
├── Journal.md                   # Journal de bord du projet
├── scr/                         # Dossier contenant les scripts
│   ├── web_scrap_lyrics         # Script pour effectuer une première partie de scraping
│   ├── scrap_genre              # Script de scraping fonctionnel par genre
│   ├── clean_data_csv           # Script pour le pré-traitement des données et la création d'un fichier csv
│   ├── stat_text                # Script de calculs statistiques sur les corpus
|   ├── algo_tests               # Script utilisé pour tester la classification sur les données et renvoyer une évaluation automatique de ces données
│   ├── increase_data            # Script permettant une augmentation du dataset
|   └── 
├── data/
|   └── raw                      # Dossier contenant les corpus par genre
│   |   ├── corpus_rap
│   |   ├── corpus_rnb
│   |   └── corpus_pop
|   └── processed                # Dossier contenant les autres fichiers utilisés comme données par des scripts
│   |   ├── lyrics.csv
│   |   ├── perf_models.csv
│   |   └── results_gridsearc.csv
├── results/                     # Dossier contenant tous les visuels et résultats
│   ├── freq_pop.png
│   ├── freq_rap.png
│   ├── freq_rnb.png
│   ├── lengths_pop.png
│   ├── lengths_rap.png
│   ├── lengths_rnb.png
│   ├── wordcloud_pop.png
│   ├── wordcloud_rap.png
│   ├── wordcloud_rnb.png
│   ├── confusion_matrix_random_forest.png
│   ├── confusion_matrix_naive_bayes.png
│   ├── confusion_matrix_svm.png
│   └── all_confusion_matrix.png
└── README.md
```

---

## Résultats et évaluations :



---

## Bibliographie :

* [Scikit-learn Documentation](https://scikit-learn.org/stable/)
* Contenu des cours d'Outils de Traitement de Corpus - Ève Sauvage
