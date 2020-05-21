from flask import Flask, jsonify, request

app = Flask(__name__)

from personalsheet import personal_sheet
from skills import skills
from languages import languages
from jobs import jobs
from equipement import equipement
from locations import locations
from mentalillness import mental_illness
from myths import myths
from nacionality import nacionality
from sanity import loss_of_sanity
from spells import spells
from weapons import weapons

@app.route("/")
def saludo():
    return("Welcome, Guardian")
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

#character's characteristics

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

@app.route('/personalsheet/<string:character_name>', methods=['DELETE'])
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

#character skills
@app.route('/skills')
def getskill():
    return jsonify({'skills': skills})

@app.route('/skills/<string:character_name>')
def getSkill(skill_name):
    for skill in skills:
        if skill['name'] == skill_name.lower():
            skillFound = skill
    print(type(skillFound))
    if (len(skillFound) > 0):
        return jsonify({'skills': skillFound})
    return jsonify({'message': 'skill not found'})

@app.route('/skills', methods=['POST'])
def addSkill():
    new_skill = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    skills.append(new_skill)
    return jsonify({'mensaje': 'Skill succesfully added', 'skill': skills})

@app.route('/skills/<string:skill_name>', methods=['PUT'])
def editSkill(skill_name):
    for skill in skills:
        if skill['name'] == skill_name.lower():
            skillFound = skill
    if (len(skillFound) > 0):
        skillFound[0]['name'] = request.json['name']
        skillFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Skill modified succesfully',
            'skill': skillFound[0]
        })
    return jsonify({'message': 'Skill not found'})

@app.route('/skills/<string:skill_name>', methods=['DELETE'])
def deleteSkill(skill_name):
    for skill in skills:
        if skill['name'] == skill_name.lower():
            skillFound = skill
    if (len(skillFound) > 0):
        skills.remove(skillFound[0])
        return jsonify({
            'message': 'Skill gone',
            'skills': skills
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)

