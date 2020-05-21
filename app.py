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

#character's languages
@app.route('/languages')
def getlanguage():
    return jsonify({'languages': languages})

@app.route('/languages/<string:lang_name>')
def getLang(lang_name):
    for lang in lang_name:
        if lang['name'] == lang_name.lower():
            langFound = lang
    print(type(langFound))
    if (len(langFound) > 0):
        return jsonify({'characteristics': langFound})
    return jsonify({'message': 'Language not found'})

@app.route('/languages', methods=['POST'])
def addLang():
    new_lang = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    languages.append(new_lang)
    return jsonify({'mensaje': 'Language succesfully added', 'languages': languages})

@app.route('/languages/<string:lang_name>', methods=['PUT'])
def editLang(lang_name):
    for lang in languages:
        if lang['name'] == lang_name.lower():
            langFound = lang
    if (len(langFound) > 0):
        langFound[0]['name'] = request.json['name']
        langFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Language modified succesfully',
            'char': langFound[0]
        })
    return jsonify({'message': 'Language not found'})

@app.route('/languages/<string:lang_name>', methods=['DELETE'])
def deleteLang(lang_name):
    for lang in languages:
        if lang['name'] == lang_name.lower():
            langFound = lang
    if (len(langFound) > 0):
        languages.remove(langFound[0])
        return jsonify({
            'message': 'Language gone',
            'language': languages
        })

#character's nacionality
@app.route('/nacionality')
def getnac():
    return jsonify({'nacionality': nacionality})

@app.route('/nacionality/<string:nac_name>')
def getNac(nac_name):
    for nac in nacionality:
        if nac['name'] == nac_name.lower():
            nacFound = nac
    print(type(nacFound))
    if (len(nacFound) > 0):
        return jsonify({'nacionality': nacFound})
    return jsonify({'message': 'Nacionality not found'})

@app.route('/nacionality', methods=['POST'])
def addNac():
    new_nac = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    nacionality.append(new_nac)
    return jsonify({'mensaje': 'Nacionality succesfully added', 'nacionality': nacionality})

@app.route('/nacionality/<string:nac_name>', methods=['PUT'])
def editNac(nac_name):
    for nac in nacionality:
        if nac['name'] == nac_name.lower():
            nacFound = nac
    if (len(nacFound) > 0):
        nacFound[0]['name'] = request.json['name']
        nacFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Nacionality modified succesfully',
            'nac': nacFound[0]
        })
    return jsonify({'message': 'Nacionality not found'})

@app.route('/nacionality/<string:nac_name>', methods=['DELETE'])
def deleteNac(nac_name):
    for nac in nacionality:
        if nac['name'] == nac_name.lower():
            nacFound = nac
    if (len(nacFound) > 0):
        nacionality.remove(nacFound[0])
        return jsonify({
            'message': 'Nacionality gone',
            'nacionality': nacionality
        })

#character's equipement

#character's weapons

#character's job

#character's spells

#character's mental illnesses

#myths

#locations
if __name__ == '__main__':
    app.run(debug=True, port=4000)

