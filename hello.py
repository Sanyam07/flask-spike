from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    import graphlab
    songs = graphlab.SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/millionsong/song_data.csv')
    print songs
    return "done"

if __name__ == "__main__":
    app.run(debug=True)



