#############################################################################
#                                                                           #
#                                                                           #
#                CONSTANT FILE                                              #
#                                                                           #
#                                                                           #
#############################################################################

## Defining the Static parameters for search::
import os
import __root__
from Scripts.nb import NaiveBayes
from Scripts.rank_classifier import RankClassifier
from Scripts.kmeans import KMeans

doc = str()
# Data path to capture data.
data_path = "./dataset/bbc/"

#
article_to_choose_from = 5
number_of_recommendation_per_article = 5
choice = 4

# Create classifier instances..
nb = NaiveBayes()
rc = RankClassifier()
kmeans = KMeans(doc)

classifier_list = [nb]


