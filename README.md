### **Social Media Text Clustering**

#### **Tabale of content**

1. Objective
2. Process
3. Run

#### **1. Objective**

The aim of the project is to cluster or group the similar social media text into same groups. Here,tweets from Twitter are consider for testing the algorithms.

#### **2. Process**

1. Data Extraction

Tweets are extracted from Twitter with keywords which may help to evaluate the clusters or groups clustered by the algorithms. The following script helps to get the data with different size of datasets from each keyword since it can not be expected same size from each keyword in real world scenario.

```
scrape_data.py
```

2. Data Cleaning and Preprocessing

Before starting the any algorithm, scrapped data should be cleaned. So, the pre-defined cleaning funtion is applied on  the data prior to fitting any kind of model, for example KMeans, LDA etc.


3. Model Fitting

- Clustering Algorithms

There are multiple Clustering algorthms were tested on the data. The following .ipynb file includes all the clustering algorithms are it's explanation which is examined on the data. Since none of these clustering techniques are useful for this particular dataset, the next step is considered.

```
Clustering.ipynb
```
- LDA Model

The most famous Topic modeling - LDA has tested on this data. It also failed to give expected output, mainly the Coherence score is not converge in any point in the number of topic in the Number of Topics Vs Coherence score. Further, Top2Vec model has examined, but most of the words in each Topic is not giving proper colclusion about the Topic. Thus, the BERTopic model is fitted to explore the topics.

```
LDA_Top2Vec_Models.ipynb
```

- BERTopic Model

This model gives the rational output of number of topics and most common words for each topic, since this model is constructed on top multiple models such as Embedding Models, UMAP,  HDBSCAN etc which an be be fine tuned separatly and called to the main BERTopic model. Further, Merge Topics option also available to merge or combine similar topics after fitting the model. The following file gives the all the explanation of the model fitting process. 
```
BERTopic-Hyperparameter.ipynb
```
#### **3. Run**

Download the project folder and run each file separatly to explore the topics given by each algorithm in colab.

If the dataset changes all the output (Topic) get changed. Thus, run all the code mainly the paramenter tuning in BERTopic model where parameters of UMAP and HDBSCAN is selected. Manual analysis is required to select those parameters.



