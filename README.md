#Nom etablissement : ISPM , Institut Supérieur Polytechnique de Madagascar

#Site de web de l'etablissement : www.ispm-edu.com

#Nom de membres de groupe Igglia : 
    #WEB 
        NOFINIAINA NATOLOJANAHARY Tambatra
        RABEMANANTSIMBA Onja Faneva Rinoh
      
    #Machine Learning :
        RAZAFINDRALAMBO Lafatra
        ANDRIAMIALINIRINA Fanantenana
        RASOLOHERISON Nambinina
        RANDIMBIARISOA Santatriniaina Charles Ricardo

#Description du stack technologiques :
    Django Python pour l'interface web,
    Pour le ML : 
        ScikitLearn, NlTK, Pandas, Numpy, joblib  

#Description du processus et du modèle :

    Dataset 
        ↓
    Prétraitement des données
        ↓
    Préparation de données
        ↓
    Vectorisation 
        ↓
    Entrainement des modèles
        ↓
    Service Python (predict_spam)
        ↓
    View Django
        ↓
    Interface Web (Bootstrap)
        ↓
    Déploiement (Render )

#Les methodes ML : 

    Apprentissage supervisé pour la classification des messages en SPAM et HAM

    Utilisation de données textuelles annotées (messages courts)

    Prétraitement du texte : mise en minuscules, suppression de la ponctuation et des mots vides (stop words)

    Représentation des messages par la méthode TF-IDF

    Utilisation de n-grammes (unigrammes et bigrammes) pour capturer le contexte

    Modèle de classification basé sur la régression logistique

    Prédiction accompagnée d’un score de confiance (probabilité)

    Évaluation des performances à l’aide de l’accuracy et du F1-score

    Intégration du modèle dans une application web Django      

#Les datasets Utilisés : 
    KaggleHUB 

#Lien vers l'application web hebergé : 
    https://spam-ham-detector-4m22.onrender.com

