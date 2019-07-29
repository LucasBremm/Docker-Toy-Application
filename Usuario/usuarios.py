from flask import Flask, jsonify

app = Flask(__name__)

usuarios = [
    {
        'id':1,
        'nome':'Lucas'
    },
    {
        'id':2,
        'nome':'Adriani'
    },
    {
        'id':3,
        'nome':'Lucian'
    },
    {
        'id':4,
        'nome':'Marcia'
    },
    {
        'id':5,
        'nome':'Eduardo'
    }
]   

@app.route('/info', methods=['GET'])
def teste():
    return jsonify(usuarios)


@app.route('/info/<int:id>', methods=['GET'])
def getinfo(id):
    for usuario in usuarios:
        if(usuario['id'] == id):
            return jsonify(usuario), 200
    
    return jsonify({'erro':'not found'}), 404

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port=2000)