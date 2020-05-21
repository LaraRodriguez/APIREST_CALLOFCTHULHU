from flask import Flask, jsonify, request

app = Flask(__name__)

from personalsheet import personal_sheet

@app.route("/")
def saludo():
    return("Bienvenido, Guardian")
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

#aqui comienzan las rutas para los datos

@app.route('/personalsheet')
def getchar():
    return jsonify({'personal sheet': personal_sheet})

@app.route('/personalsheet/<string:character_name>')
def getCharacter(character_name):
    for char in personal_sheet:
        if char['name'] == character_name.lower():
            charFound = char
    print(type(charFound))
    if (len(charFound) > 0):
        return jsonify({'characteristics': charFound})
    return jsonify({'message': 'Characteristic not found'})

@app.route('/personalsheet', methods=['POST'])
def addChar():
    new_char = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    personal_sheet.append(new_char)
    return jsonify({'mensaje': 'Characteristc succesfully added', 'personalsheet': personal_sheet})

@app.route('/personalsheet/<string:character_name>', methods=['PUT'])
def editChar(character_name):
    for char in personal_sheet:
        if char['name'] == character_name.lower():
            charFound = char
    if (len(charFound) > 0):
        charFound[0]['name'] = request.json['name']
        charFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Characteristic modified succesfully',
            'char': charFound[0]
        })
    return jsonify({'message': 'Characteristic not found'})

@app.route('/products/<string:character_name>', methods=['DELETE'])
def deleteChar(character_name):
    for char in personal_sheet:
        if char['name'] == character_name.lower():
            charFound = char
    if (len(charFound) > 0):
        personal_sheet.remove(charFound[0])
        return jsonify({
            'message': 'Characteristic gone',
            'personalsheet': personal_sheet
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)

