import numpy as np
import pickle as pkl

similar_score=pkl.load(open('Learn/Book_recommendation/similar_score.pkl','rb'))
pt=pkl.load(open('Learn/Book_recommendation/pt.pkl','rb'))
books=pkl.load(open('Learn/Book_recommendation/books.pkl','rb'))

def recommend_func(book_name):
    book_name=book_name.strip()
    if book_name in pt.index:
        index=np.where(pt.index==book_name)[0][0]
        similar=sorted(list(enumerate(similar_score[index])),key=lambda x:x[1],reverse=True)[2:10]
        l=[]
        for i in similar:
            temp_df=books[books['Book-Title']==pt.index[i[0]]]
            # temp_df=temp_df.drop_duplicates(subset=['Book-Title'])
            temp_df=temp_df[['Book-Title','Book-Author','Image-URL-M']]
            l.append(temp_df.to_numpy()[0])
        return l
    