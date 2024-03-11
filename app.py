from flask import Flask,render_template,request
import pickle as pkl
import pandas as pd
import numpy as np
from func.recommend import recommend_func as rc

app=Flask(__name__)

popular_df=pkl.load(open('popular.pkl','rb'))
similar_score=pkl.load(open('similar_score.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/topbooks')
def topbooks():
    return render_template('topbooks.html',books=popular_df.to_numpy())

@app.route('/recommender',methods=['GET','POST'])
def recommend_flask():
    if request.method=='GET':
        return render_template('recommend.html')
    elif request.method=='POST':
        input_book=request.form['input_book']
        print(input_book)
        l=rc(input_book)
        print(l)
        return render_template('recommend.html',rc_books=l)

if __name__=='__main__':
    app.run(debug=True)