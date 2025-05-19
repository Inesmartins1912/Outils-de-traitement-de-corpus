# Projet d'Outils de traitement de corpus

**Tâche choisie : Classification de chansons par genre à partir des paroles**

## Description

Ce projet a pour objectif de classifier automatiquement des chansons par genre musical (rap, rock et reggae) sur la base de l'analyse de leurs paroles uniquement. Le modèle ne dispose ainsi ni de la musique ni de métadonnées pouvant lui donner des indices pour la classification : il se base exclusivement sur le contenu lexical des textes.

Pour ce faire il faut dans un premier temps constituer un corpus d'environ 300 chansons en anglais (100 par genre musical pour une question d'équilibre du jeu de données), à l'aide d'un scrip permettant de scraper depuis le web. Puis dans un deuxième temps il faut appliquer au corpus des scripts de prétraitement, vectorisation, analyse exploratoire et classification supervisée à l’aide de la bibliothèque scikit-learn (et Weka éventuellement pour comparaison).

---

## Contenu du dépôt :

```
Outils_de_traitement_de_corpus/
├── Journal.md                   # Journal de bord du projet
├── scr/                         # Dossier contenant les scripts
│   ├── web_scrap_lyrics         # Script pour effectuer le scraping soit la récupération des paroles
│   ├── clean_data_csv           # Script pour le pré-traitement des données et la création d'un fichier csv
│   ├──                          # Script
|   └──                          # Script
├── corpus/                      # Dossier contenant les corpus par genre
│   ├── corpus_rap
│   ├── corpus_rock
│   └── corpus_reggae
├── results/
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   └──  
├── tableaux/
│   ├── 
│   └── lyrics.csv               # Corpus nettoyé prêt à être utilisé
└── README.md
```

---

## Résultats et évaluations :



---

## Bibliographie :

* [Scikit-learn Documentation](https://scikit-learn.org/stable/)
* [Weka Wiki](https://waikato.github.io/weka-wiki/)
* Contenu des cours d'Outils de Traitement de Corpus - Ève Sauvage
