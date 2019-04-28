

def fillPokemon_has_Move(databasename):
    """
       This Function will open the specific JSON Pokemon Data File which was choosed by the User / Admin. Based on this Data it's looking
       for the Pokemon and SELECT the pokemon_id from the pokemon table and the  move_id from the Table Move. For every move and Pokemon
       in the JSON FILE there will be a INSERT INTO Statement to fill the Pokemon_has_Move Table in addition with percentage from the JSON FILE.
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
    u = 725
    for pokemon in data["data"]:
        print(pokemon)
        mycursor.execute("SELECT poke_id FROM Pokemon WHERE pokemonName = '%s'" %pokemon)
        pokemonid = mycursor.fetchone()
        for move in data["data"][pokemon]["Moves"]:
            if move=="":
                pass
            else:
                mysecondcursor.execute("SELECT move_id FROM Move WHERE move_Name = '%s'" % move)
                moveid = mysecondcursor.fetchone()
                if moveid is None:
                    mycursor.execute('INSERT INTO Move(move_id,move_Name) VALUES (%s,%s)', (u, move))
                    mysecondcursor.execute("SELECT move_id FROM Move WHERE move_Name = '%s'" % move)
                    moveid = mysecondcursor.fetchone()
                    u = u + 1
                    percentage = data["data"][pokemon]["Moves"][move]
                    mycursor.execute('INSERT INTO Pokemon_has_Move(poke_id,move_id,percentage) VALUES (%s,%s,%s)',(pokemonid[0], moveid[0], percentage))
                    mydb.commit()
                else:
                    percentage = data["data"][pokemon]["Moves"][move]
                    mycursor.execute('INSERT INTO Pokemon_has_Move(poke_id,move_id,percentage) VALUES (%s,%s,%s)',(pokemonid[0], moveid[0], percentage))
                    mydb.commit()