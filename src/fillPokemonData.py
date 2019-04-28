



def fillPokemon(databasename):
    """
           This Function will open the specific JSON Pokemon Data File which was choosed by the User / Admin. Based on this Data it's looking
           going through all Pokemon in this File. For every Pokemon
           in the JSON FILE there will be a INSERT INTO Statement to fill the Pokemon Table in addition with the usage-rate of this Pokemon
           :param databasename:
           :return:
           """
    import json
    import mysql.connector

    with open('dbdatafile.json') as test:
        data = json.load(test)
    i = 1
    mydb = mysql.connector.connect(
        host="XXX.XXX.XXX.XXX",
        user="XXX",
        passwd="XXX",
        database=databasename)
    mycursor = mydb.cursor()
    for pokemon in data["data"]:
        mycursor.execute('INSERT INTO Pokemon(poke_id,pokemonName,rate) VALUES (%s,%s,%s)', (i, pokemon,data["data"][pokemon]["usage"]))
        i = i +1
        mydb.commit()



