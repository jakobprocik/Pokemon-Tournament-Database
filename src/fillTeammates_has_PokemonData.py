import json





def fillTeammates_has_Pokemon(databasename):
    """
    This Function will Loop through the JSON File and find all possible candidates for a Teampartner(mate) to a specific Pokemon.
    Its basicly looking for the Pokemon and their pokemon_id and is looking for his mate with his own mate_id. Sometimes there are Pokemon not in the Database
    like new Pokemon, so I had to catch that and add them. After that INSERT the Pokemon pokemon_id with his Mate mate_id and the percentage rate.
    :param databasename:
    :return:
    """
    import mysql.connector

    with open('dbdatafile.json') as test:
        data = json.load(test)
    u = 811
    mydb = mysql.connector.connect(
        host="XXX.XXX.XXX.XXX",
        user="XXX",
        passwd="XXX",
        database=databasename)
    mycursor = mydb.cursor()
    mysecondcursor = mydb.cursor()
    for pokemon in data["data"]:
        mycursor.execute("SELECT poke_id FROM Pokemon WHERE pokemonName = '%s'" %pokemon)
        pokemonid = mycursor.fetchone()
        for mate in data["data"][pokemon]["Teammates"]:
            copymate = mate.replace("'","")
            mysecondcursor.execute("SELECT mate_id FROM Teammates WHERE pokemonName = '%s'" %copymate)
            mateid = mysecondcursor.fetchone()
            if mateid is None:
                mycursor.execute('INSERT INTO Teammates(mate_id,pokemonName) VALUES (%s,%s)', (u, copymate))
                mysecondcursor.execute("SELECT mate_id FROM Teammates WHERE pokemonName = '%s'" % copymate)
                mateid = mysecondcursor.fetchone()
                u = u +1
                percentage = data["data"][pokemon]["Teammates"][mate]
                mycursor.execute('INSERT INTO Pokemon_has_Teammates(poke_id,mate_id,percantage) VALUES (%s,%s,%s)',(pokemonid[0], mateid[0], percentage))
            else:
                percentage = data["data"][pokemon]["Teammates"][mate]
                mycursor.execute('INSERT INTO Pokemon_has_Teammates(poke_id,mate_id,percantage) VALUES (%s,%s,%s)', (pokemonid[0], mateid[0],percentage))
                mydb.commit()






