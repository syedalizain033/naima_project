from flask import Flask
app=Flask("__main__")

@app.route('/')
def home():
    return "Hello Naima World."

if __name__=="__main__":
    app.run(host="0.0.0.0")