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

La récupération du corpus de travail ne s'est apas passée comme prévue, en effet je voulais tout d'abord scraper les artistes, puis les titres et enfin les paroles mais cela ne fonctionnait pas malgré de multiples modifications, je me suis donc retrouvée avec la partie permettant de scraper des artistes qui fonctionnait et le reste non, afin de pouvoir tout de même rendre ce projet j'ai donc été contrainte d'utiliser l'API Genius pour les parties titres de chansons et paroles.
De plus le scraping me renvoyait des noms d'artistes pour lesquels aucune chanson n'était retournée j'ai donc été obligée par manque de temps de créer des listes d'artistes manuellement pour que les scripts fonctionnent.

## TP3 : Pré-traitement des données et statistiques de texte

Pour la visualisation du corpus, j'ai fait d'utiliser un script qui nettoie et transforme mes corpus en csv dans le but de pouvoir 
1. longueur des textes
2. mots fréquents (zipf)
3. les statistiques adaptées à votre tâche

## TP4 : 

A partir des données que vous avez récupérées, augmentez vos données en créant un dataset synthétique.
Choississez l’architecture adaptée à votre tâche et trouvez un modèle qui correspond à votre tâche et à cette architecture.

## TP5 :

Finetuner le modèle pretrained qui correspond le plus à vos données grâce au trainer d’hugging face

## TP6 :

Evaluer votre modèle
