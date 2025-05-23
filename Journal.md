# Journal de bord de Projet d'Outils de traitement de corpus 

## TP1 : Choix de la tâche

**Besoins du projet :** Ce projet nécessitera un corpus relativement vaste, je pense 300 textes au total, 100 par genre.  
**Dans quel besoin le projet s'inscrit ? :** Savoir dans quel genre se classe une chanson uniquement à partir des paroles.  
**Quel sujet allez vous traiter ? :** La classification automatique de chansons par genre à partir des paroles.  
**Quel type de tâche allez vous réaliser ? :** La tâche réalisée est une tâche de classifcation.  
**Quel type de données allez vous exploiter ? :** Des données textuelles étant des paroles de chansons de plusieurs genres.  
**Où allez vous récupérer vos données ? :** Divers sites pour trouver d'abord les artistes par genre, puis les titres des chansons et ensuite les paroles de chaque chanson.  
**Sont-elles libres d’accès ? :** Ces données sont libres d'accès.  

## TP2 : Web-Scraping 

La récupération du corpus de travail ne s'est pas passée comme prévue, en effet je voulais tout d'abord scraper les artistes, puis les titres et enfin les paroles mais cela ne fonctionnait pas bien malgré de multiples modifications je me retrouvais toujours avec des scraps vides ou bien complètement bloquée, je me suis donc retrouvée avec la partie permettant de scraper des artistes qui fonctionnait et le reste non. Ayant perdu beaucoup de temps sur cette étape et afin de pouvoir tout de même rendre ce projet j'ai donc été contrainte d'utiliser l'API Genius pour les parties titres de chansons et paroles car je ne me voyais pas changer de sujet en ayant déjà avancé tous les autres scripts en parallèle.  

De plus le scraping me renvoyait des noms d'artistes pour lesquels aucune chanson n'était retournée j'ai donc été obligée par manque de temps de créer des listes d'artistes manuellement pour que les scripts fonctionnent et de changer de genres en me rabattant sur des genres plus populaires et que j'avais déjà abordés préalablement au cours d'un autre projet c'est-à-dire le rap, la pop et le R&B.

## TP3 : Pré-traitement des données et statistiques

Pour la visualisation du corpus, j'ai fait le choix d'utiliser dans un premier temps un script qui nettoie et transforme mes corpus en csv dans le but de pouvoir utiliser ce fichier dans la réalisation de certaines visualisations (wordclouds).
1. longueur des textes
2. mots fréquents (zipf)
3. un nuage de mots pour une visualisation des mots les plus fréquents

## TP4 : Augmentation des données

Les données récupérées forment déjà un dataset synthétique avec 100 chansons par genre cependant le script ```algo_test``` permet de le scinder en plusieurs morceaux pour avoir un corpus_train et un corpus_test afin d'effectuer l'entraînement et les tests des modèles. En effet, dans le cadre de ce projet pluseurs modèles de la bibliothèque ```scikitlearn``` de Python ont été utilisé :
- Random Forest (arbres de décisions)
- Naive Bayes
- SVM
Cependant étant donné que ce TP traitait de l'augmentation du dataset je vais tout de même créer un script ```increase_data``` permettant de faire cela. Ce script génère donc un corpus de 60 txt supplémentaires à partir de fichiers .txt déjà existants (classés par genre : pop, rap ou rnb). Pour chaque genre, il sélectionne aléatoirement 4 lignes de plusieurs textes (en ignorant les premières lignes qui sont souvent dans les paroles de chansons peu importante en termes de contenu pour l'analyse), puis combine ces extraits pour créer de nouveaux fichiers .txt par genre. Ces fichiers sont ensuite enregistrés dans un dossier corpus_increase, organisé par genre. Le but est d’augmenter les données d’entraînement avec des exemples réalistes mais générés de manière artificielle qui pourraient donc être utilisées pour l'analyse même si je ne le fais pas ici.

## TP5 : Finetuning du trainer d'hugging face

Finetuner le modèle pretrained qui correspond le plus à vos données grâce au trainer d’hugging face

## TP6 : Évaluation de mon modèle 

Pour ce qui est de l'évaluation du modèle le script ```algo_test``` renvoie des matrices de confusion pour plusieurs modèles testés (Random Forest, Naive Bayes et SVM), ainsi que leurs résultats de performances que l'on retrouve dans perf_models.csv. On peut conclure de ces résultats ainsi que des matrices de confusion que ces modèles sont relativemet performant. En effet, on remarque plusieurs choses :  
- Tout d'abord, le genre rap est plus facilement identifiable, avec un lexique que semble se diversifier des deux autres genres, ce qui était également visible dans les premiers visuels (schéma des fréquences et wordclouds). Alors que d'autre part la pop et le R&B semblent lexicalement très proches, ce qui les rend plus difficlement identifiables et classifiables pour le modèle.   
- Pour ce qui est des résultats de preformances on obtient les taux de précision globale (accuracy) suivants :   
    - Naive Bayes: Accuracy moyenne = 0.5865 | Écart-type = 0.0325  
    - SVM: Accuracy moyenne = 0.5730 | Écart-type = 0.0369  
    - Random Forest: Accuracy moyenne = 0.5820 | Écart-type = 0.0401  
  On peut donc constater une légère différence entre les trois modèles avec Naive Bayes ayant un taux de précision global très haut et l'écart-type le plus faible, et SVM et Random Forect un peu moins fiable   avec un taux de précision plus faible pour SVM mais un écart-type plus grand pour les arbres de décisions.  
