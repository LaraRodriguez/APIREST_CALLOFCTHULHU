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
@app.route('/equipement')
def getequip():
    return jsonify({'equipement': equipement})

@app.route('/equipement/<string:equip_name>')
def getEquip(equip_name):
    for equip in equipement:
        if equip['name'] == equip_name.lower():
            equipFound = equip
    print(type(equipFound))
    if (len(equipFound) > 0):
        return jsonify({'Equipement': equipFound})
    return jsonify({'message': 'Equipement not found'})

@app.route('/equipement', methods=['POST'])
def addEquip():
    new_equip = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    equipement.append(new_equip)
    return jsonify({'message': 'Equipement succesfully added', 'equipement': equipement})

@app.route('/equipement/<string:equip_name>', methods=['PUT'])
def editEquip(equip_name):
    for equip in equipement:
        if equip['name'] == equip_name.lower():
            equipFound = equip
    if (len(equipFound) > 0):
        equipFound[0]['name'] = request.json['name']
        equipFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Equipement modified succesfully',
            'equip': equipFound[0]
        })
    return jsonify({'message': 'Equipement not found'})

@app.route('/equipement/<string:equip_name>', methods=['DELETE'])
def deleteEquip(equip_name):
    for equip in equipement:
        if equip['name'] == equip_name.lower():
            equipFound = equip
    if (len(equipFound) > 0):
        equipement.remove(equipFound[0])
        return jsonify({
            'message': 'Equipement gone',
            'equipement': equipement
        })

#character's weapons
@app.route('/weapons')
def getwea():
    return jsonify({'weapons': weapons})

@app.route('/weapons/<string:weapons_name>')
def getWea(wea_name):
    for wea in weapons:
        if wea['name'] == wea_name.lower():
            weaFound = wea
    print(type(weaFound))
    if (len(weaFound) > 0):
        return jsonify({'weapons': weaFound})
    return jsonify({'message': 'Weapon not found'})

@app.route('/weapon', methods=['POST'])
def addWea():
    new_wea = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    weapons.append(new_wea)
    return jsonify({'message': 'Weapon succesfully added', 'weapon': weapons})

@app.route('/weapons/<string:wea_name>', methods=['PUT'])
def editWea(wea_name):
    for wea in weapons:
        if wea['name'] == wea_name.lower():
            weaFound = wea
    if (len(weaFound) > 0):
        weaFound[0]['name'] = request.json['name']
        weaFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Weapon modified succesfully',
            'wea': weaFound[0]
        })
    return jsonify({'message': 'Weapon not found'})

@app.route('/weapons/<string:wea_name>', methods=['DELETE'])
def deleteWea(wea_name):
    for wea in weapons:
        if wea['name'] == wea_name.lower():
            weaFound = wea
    if (len(weaFound) > 0):
        weapons.remove(weaFound[0])
        return jsonify({
            'message': 'Weapon gone',
            'weapon': weapons
        })

#character's job
@app.route('/jobs')
def getjob():
    return jsonify({'job': jobs})

@app.route('/jobs/<string:job_name>')
def getJob(job_name):
    for job in jobs:
        if job['name'] == job_name.lower():
            jobFound = job
    print(type(jobFound))
    if (len(jobFound) > 0):
        return jsonify({'jobs': jobFound})
    return jsonify({'message': 'Jobs not found'})

@app.route('/jobs', methods=['POST'])
def addJob():
    new_job = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    jobs.append(new_job)
    return jsonify({'message': 'Job succesfully added', 'job': jobs})

@app.route('/jobs/<string:job_name>', methods=['PUT'])
def editJob(job_name):
    for job in jobs:
        if job['name'] == job_name.lower():
            jobFound = job
    if (len(jobFound) > 0):
        jobFound[0]['name'] = request.json['name']
        jobFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Job modified succesfully',
            'job': jobFound[0]
        })
    return jsonify({'message': 'Job not found'})

@app.route('/jobs/<string:job_name>', methods=['DELETE'])
def deleteJob(job_name):
    for job in jobs:
        if job['name'] == job_name.lower():
            jobFound = job
    if (len(jobFound) > 0):
        jobs.remove(jobFound[0])
        return jsonify({
            'message': 'Job gone',
            'job': jobs
        })

#character's spells
@app.route('/spells')
def getspell():
    return jsonify({'spell': spells})

@app.route('/spells/<string:spell_name>')
def getSpell(spell_name):
    for spell in spells:
        if spell['name'] == spell_name.lower():
            spellFound = spell
    print(type(spellFound))
    if (len(spellFound) > 0):
        return jsonify({'spell': spellFound})
    return jsonify({'message': 'Spell not found'})

@app.route('/spells', methods=['POST'])
def addSpell():
    new_spell = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    spells.append(new_spell)
    return jsonify({'message': 'Spell succesfully added', 'spell': spells})

@app.route('/spells/<string:spell_name>', methods=['PUT'])
def editSpell(spell_name):
    for spell in spells:
        if spell['name'] == spell_name.lower():
            spellFound = spell
    if (len(spellFound) > 0):
        spellFound[0]['name'] = request.json['name']
        spellFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Spell modified succesfully',
            'spell': spellFound[0]
        })
    return jsonify({'message': 'spell not found'})

@app.route('/spells/<string:spell_name>', methods=['DELETE'])
def deleteSpell(spell_name):
    for spell in spells:
        if spell['name'] == spell_name.lower():
            spellFound = spell
    if (len(spellFound) > 0):
        spells.remove(spellFound[0])
        return jsonify({
            'message': 'Abracadabra, spell gone',
            'spell': spells
        })

#character's mental illnesses
@app.route('/mentalillness')
def getill():
    return jsonify({'mental illnesses': mental_illness})

@app.route('/mentalillness/<string:ill_name>')
def getIll(ill_name):
    for ill in mental_illness:
        if ill['name'] == ill_name.lower():
            illFound = ill
    print(type(illFound))
    if (len(illFound) > 0):
        return jsonify({'mental illnesses': illFound})
    return jsonify({'message': 'Mental illness not found'})

@app.route('/mentalillness', methods=['POST'])
def addIll():
    new_ill = {
        'name': request.json['name'],
        'description': request.json['description']
    }
    mental_illness.append(new_ill)
    return jsonify({'message': 'Mental illness succesfully added', 'mental illness': mental_illness})

@app.route('/mentalillness/<string:ill_name>', methods=['PUT'])
def editIll(ill_name):
    for ill in mental_illness:
        if ill['name'] == ill_name.lower():
            illFound = ill
    if (len(illFound) > 0):
        illFound[0]['name'] = request.json['name']
        illFound[0]['description'] = request.json['description']
        return jsonify({
            'message': 'Mental illness modified succesfully',
            'ill': illFound[0]
        })
    return jsonify({'message': 'Mental illness not found'})

@app.route('/mentalillness/<string:ill_name>', methods=['DELETE'])
def deleteIll(ill_name):
    for ill in mental_illness:
        if ill['name'] == ill_name.lower():
            illFound = char
    if (len(illFound) > 0):
        mental_illness.remove(charFound[0])
        return jsonify({
            'message': 'Mental illness gone',
            'mental illness': mental_illness
        })

#myths

#locations
if __name__ == '__main__':
    app.run(debug=True, port=4000)

