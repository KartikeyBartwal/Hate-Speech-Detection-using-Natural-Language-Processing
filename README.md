[steps to run.webm](https://github.com/KartikeyBartwal/Hate-Speech-Detection-using-Natural-Language-Processing/assets/98084657/72740adb-51b8-4058-95c2-27caef14cd4c)# Project

Created a model to classify text messages in one of the 3 categories:
1) Hate speech and offensive
2) Safe speech


## About the Dataset

The dataset utilizes Twitter data and was employed for researching hate speech detection. The text within this dataset is classified as hate speech, offensive language, or neither. It's important to note that, due to the nature of the study, this dataset contains text that may be considered racist, sexist, homophobic, or generally offensive.


## Data features:
1) Count: Total number of people who voted for this
2) hate_speech: Number of people who voted for the tweet to be a hate speech
3) offensive_language: number of people who voted for the tweet to be an offensive_language
4) neither: number of people who voted for the tweet to be neither hate_speech nor offensive
5) class: The final category of the tweet decided from the votings. 
    0 -> Hate speech
    1 -> Offensive langugae
    2 -> Neither
    
    
## Machine Learning Techniques Applied 
1) Natural Langugae Processing
2) Feature engineering: tokenization, count vectorization, data splitting, text formatting using basic data cleaning tehniques using the nltk library
3) Random forest regressor algorithm to train the machine on the training data
4) Performance metrics using training data and testing data accuracy, confusion matrix, classification report
5) Saving the model in pickle format to be usable anytime and anywhere
6) Model is ready to be deployed and used in any real time environment, as a microservice feature and what not
