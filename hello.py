from flask import Flask
app=Flask(__name__)
@app.route('/')
def firstApp():
    return "hello welcome!"
if __name__ =='__main__':
    app.run(debug=True)