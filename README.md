# SMS Detect Spam & Ham

## Informations sur l'établissement

*   **Nom de l'établissement :** ISPM, Institut Supérieur Polytechnique de Madagascar
*   **Site web de l'établissement :** [www.ispm-edu.com](http://www.ispm-edu.com)

## Membres du groupe IGGLIA5

### WEB
*   NOFINIAINA NATOLOJANAHARY Tambatra
*   RABEMANANTSIMBA Onja Faneva Rinoh

### Machine Learning
*   RAZAFINDRALAMBO Lafatra
*   ANDRIAMIALINIRINA Fanantenana
*   RASOLOHERISON Nambinina
*   RANDIMBIARISOA Santatriniaina Charles Ricardo

## Description du stack technologique

*   **Django Python** pour l'interface web.
*   **Pour le ML :** Scikit-Learn, NLTK, Pandas, NumPy, joblib.

## Description du processus et du modèle

1.  **Dataset**
2.  **Prétraitement des données**
3.  **Préparation des données**
4.  **Vectorisation**
5.  **Entraînement des modèles**
6.  **Service Python** (`predict_spam`)
7.  **View Django**
8.  **Interface Web** (Bootstrap)
9.  **Déploiement** (Render)

## Les méthodes ML

*   Apprentissage supervisé pour la classification des messages en SPAM et HAM.
*   Utilisation de données textuelles annotées (messages courts).
*   Prétraitement du texte : mise en minuscules, suppression de la ponctuation et des mots vides (*stop words*).
*   Représentation des messages par la méthode TF-IDF.
*   Utilisation de n-grammes (unigrammes et bigrammes) pour capturer le contexte.
*   Modèle de classification basé sur la régression logistique.
*   Prédiction accompagnée d’un score de confiance (probabilité).
*   Évaluation des performances à l’aide de l’accuracy et du F1-score.
*   Intégration du modèle dans une application web Django.

## Les datasets utilisés

*   KaggleHUB : Multi-spam 

## Lien vers l'application web hébergée

[https://spam-ham-detector-4m22.onrender.com](https://spam-ham-detector-4m22.onrender.com)
