# News Search Engine

An information retrieval project that returns relevant news from its database based on the users' queries.

# Introduction
This project consists of three phases which are explained below. 

## Phase One: Pre-processing, inverted indexes
The parts of this phase are listed below.
* Pre-processing
  * Deleting the stop words
  * Deleting the punctuations
  * Tokenizing the texts
  * Normalizing the words by doing the process of stemming and lemmatization
* Building Inverted Indexes
* Answering multi word queries but without ranking the results

## Phase Two: TF-IDF, Champion Lists
In this phase, the search engine uses more advanced techniques such as tf-idf vectoring and using champion lists.
To return the results faster, in this phase more than using tf-idf I used a champion list for elements in the inverted index.
At the end, the similarity was measured using the cosine similarity method.

## Phase Three: K-means, KNN
Some machine learning methods were used in this phase to make the engine faster.
* K-means Clustering: I used k-means to cluster the documents into smaller groups, so when a new query arrives I only check its relevance with the center of each cluster and then return the most relevant results from the members of that center. This way there is no need to compare the query with all the documents and I can return the relevant results much faster.
* KNN Classification: Using the KNN classification algorithm I classified the documents into different groups and like the last part searched only in the most relevant group.
