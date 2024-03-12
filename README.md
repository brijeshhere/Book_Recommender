# Book Recommender: Collaborative Filtering based Recommender System

Link to project:
[Render](https://book-recommender-6rig.onrender.com)

Recommender systems are algorithms aimed at suggesting relevant items to users (items being movies to watch, text to read, products to buy or anything else depending on industries).

![GIF](src/Animation.gif)

Links on Website:

Top Books: Show top 50 books from the data based on user reviews
Recommender: Recommend book based on input book

Technology Used:

1. Flask
2. HTML
3. CSS
4. Python
5. Sql

Libraries Used:

1. Flask
2. Pickle
3. Pandas
4. Numpy
5. sklearn

About Data:

The Book-Crossing dataset comprises 3 files.

1. Users
Contains the users. Note that user IDs (User-ID) have been anonymized and map to integers. Demographic data is provided (Location, Age) if available. Otherwise, these fields contain NULL-values.

2. Books
Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book-Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.

3. Ratings
Contains the book rating information. Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0.