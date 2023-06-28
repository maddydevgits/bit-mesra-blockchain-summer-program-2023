from flask import Flask,request

# create an object
api=Flask(__name__)

@api.route('/')
def home():
    return('API Server is Online')

# create api for casting vote
@api.route('/castvote',methods=['get','post'])
def castvote():
    id=request.args.get('id')
    print(id)
    return ('You have voted for {0}'.format(id))


if __name__=="__main__":
    api.run(
        host='0.0.0.0',
        port=5001,
        debug=True
    )
