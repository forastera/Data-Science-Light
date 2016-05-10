# Congratulations! 
# You've just been hired to lead the data science efforts at DataSciencester, the social network for data scientists.
# This is what the network looks like (toy data set 1):

users = [
  {"id":0, "name":"Hero"},
  {"id":1, "name":"Dunn"},
  {"id":2, "name":"Sue"},
  {"id":3, "name":"Chi"},
  {"id":4, "name":"Thor"},
  {"id":5, "name":"Clive"},
  {"id":6, "name":"Hicks"},
  {"id":7, "name":"Devin"},
  {"id":8, "name":"Kate"},
  {"id":9, "name":"Klein"}
]

# As a data scientist, you know that you might enjoy meeting users with similar interests.
# Your task is to find out which users have the same interests. 
# Question: what interests do users share (and vice versa)?
# Here's a list of iser ids and their respective interests (toy data set 2):

interests = [
  (0, "Hadoop"), (0, "Big Data"), (0, "Spark"),
  (1, "Python"), (1, "MongoDB"), (1, "scikit-learn"),
  (2, "numpy"), (2, "R"), (2, "Python"), (2, "pandas"),
  (3, "statistics"), (3, "probability"), (3, "regression"),
  (4, "machine learning"), (4, "regression"), (4, "decision trees"),
  (5, "R"), (5, "Python"), (5, "statistics"),
  (6, "probability"), (6, "mathematics"), (6, "machine learning"),
  (7, "machine learning"), (7, "scikit-learn"), (7, neural networks),
  (8, "Big Data"), (8, "artificial intelligence"), (8, "hadoop"),
  (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# Step 1: build a function that finds users with a certain interest
# (hint: it's better to use an index, as in key value pairs (data structures: dictionary, defaultdict))
# Step 2: iterate over the user's interests: for each interest, iterate over the other users with that interest
# Step 3: keep count of how many times we see each user
# Step 4: Print out each interest and all the users that have this interest in common 
# (optional) Use a counter to find out which interest comes up most often. 
# (optional) Print out the list of interests in descending order of frequency.


# your solution:
