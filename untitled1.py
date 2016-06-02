from flask import Flask, render_template
app= Flask(__name__)

class Movie:
    def __init__(self,title,img):
        self.title=title
        self.img=img
movie1=Movie('Avenger','http://cdn2-www.comingsoon.net/assets/uploads/2015/03/avengersorder5.jpg')
movie2=Movie('Zootopia','http://image.phimmoi.net/film/3259/poster.medium.jpg')
movie_list=[
    movie1,
    movie2,
    Movie('Lion King','https://upload.wikimedia.org/wikipedia/en/2/23/LionKingCharacters.jpg')]

@app.route('/')
def hello_world():
    return 'Hello Minh!'
@app.route('/new')
def hello_new():
    return 'Hello New!'
@app.route('/old')
def hello_old():
    return 'Hello Old'

@app.route('/<name>')
def hello(name):
    return'Hello '+name
@app.route('/movie')
def get_movie():
    return render_template('movies.html')
@app.route('/movie2')
def get_movie2():
    return render_template('movies.html', title="Civil War", img ="https://sohanews2.vcmedia.vn/k:2016/photo-1-1461923029314/civil-war-phien-toa-ly-di-the-ky.jpg")
@app.route('/new_movies')
def movies():
    return render_template('movies.html',movie_list=movie_list)
if __name__=='__main__':
    app.run()
