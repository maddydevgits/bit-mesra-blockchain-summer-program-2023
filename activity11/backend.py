from flask import Flask,request

# create an object
api=Flask(__name__)

@api.route('/')
def home():
    return('API Server is Online')


if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=5001,
        debug=True
    )
