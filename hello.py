from flask import Flask
app=Flask(__name__)
@app.route('/')
def firstApp():
    return "hello welcome to github!"
if __name__ =='__main__':
    app.run(debug=True)
