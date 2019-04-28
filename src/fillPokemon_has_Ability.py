


def fillPokemon_hold_Ability(databasename):
    """
    This Function will open the specific JSON Pokemon Data File which was choosed by the User / Admin. Based on this Data it's looking
    for the Pokemon and SELECT the pokemon_id from the pokemon table and the  ability_id from the Table ability. For every ability and Pokemon
    in the JSON FILE there will be a INSERT INTO Statement to fill the Pokemon_has_ability Table in addition with percentage from the JSON FILE.
    :param databasename:
    :return:
    """
    import json
    import mysql.connector

    with open('dbdatafile.json') as test:
        data = json.load(test)
    mydb = mysql.connector.connect(
        host="XXX.XXX.XXX.XXX",
        user="XXX",
        passwd="XXX",
        database=databasename)
    mycursor = mydb.cursor()
    mysecondcursor = mydb.cursor()
    for pokemon in data["data"]:
        print(pokemon)
        mycursor.execute("SELECT poke_id FROM Pokemon WHERE pokemonName = '%s'" % pokemon)
        pokemonid = mycursor.fetchone()
        for ability in data["data"][pokemon]["Abilities"]:
            print(ability)
            mysecondcursor.execute("SELECT ability_id FROM Ability WHERE ability_Name = '%s'" % ability)
            abilityid = mysecondcursor.fetchone()
            percentage = data["data"][pokemon]["Abilities"][ability]
            mycursor.execute('INSERT INTO Pokemon_has_Ability(poke_id,ability_id,percentage) VALUES (%s,%s,%s)',(pokemonid[0], abilityid[0], percentage))
            mydb.commit()