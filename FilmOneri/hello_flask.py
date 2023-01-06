from flask import Flask, render_template,request
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app=Flask(__name__) 
movies_data = pd.read_csv('movies.csv')
movies_data.head()
movies_data.shape
gereklibolumler = ['genres','keywords','tagline','cast','director']
isim=movies_data["original_title"]
for ozellik in gereklibolumler:
     movies_data[ozellik] = movies_data[ozellik].fillna('')


@app.route('/') 
def entry_page()->'html':
    return render_template('anasayfa.html',page_title='Film Öneri Sistemi')


@app.route('/sum', methods=['POST'])
def sum():
  movie_name = request.form['movie']
  
  recommendations = get_recommended_movies(movie_name)  # Get the recommended movies
  return render_template('sonuc_sayfasi.html', page_title='Film önerileri', movie=movie_name, recommendations=recommendations,isim=isim)
  
@app.route('/filmlistesi', methods=['POST'])
def film():
    isim= movies_data["original_title"]
    return render_template('movielist.html', films=isim)
  

def get_recommended_movies(movie_name):
    isim= movies_data["original_title"]
    tum_ozellikler = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
    # metin verilerini özellik vektörlerine dönüştürme
    vectorizer = TfidfVectorizer()
    ozellik_vektoru = vectorizer.fit_transform(tum_ozellikler)

    #Kosinüs benzerliği veya kosinüs çekirdeği, benzerliği X ve Y'nin normalleştirilmiş nokta çarpımı olarak hesaplıyor
    similarity = cosine_similarity(ozellik_vektoru)


    list_of_all_titles = movies_data['title'].tolist()

    
    find_close_match = difflib.get_close_matches(movie_name , list_of_all_titles)
   
    close_match = find_close_match[0]
     
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    i = 1
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
  
    recommended_movies = []
    for movie in sorted_similar_movies:
     index = movie[0]
     title_from_index = movies_data[movies_data.index==index]['title'].values[0]
     recommended_movies.append(title_from_index)

    gosterilecekfilmler=[]
    for a in range(30):
      gosterilecekfilmler.append(recommended_movies[a+1])

    return gosterilecekfilmler
app.run(debug=True)