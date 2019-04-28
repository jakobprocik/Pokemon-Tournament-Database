




def fillPokemon_has_Spread(databasename):
    """
    Filling the Pokemon_has_Spread SQL Table with Input from the downloaded JSON File from PokemonShowdown.
    This Function is parsing through the JSON FILE and SELECT via the MySQL.connector the poke_id from the Table Pokemon
    where the Pokemon is the current Pokemon from the JSON File. Then it looks after the spread_id from Table Spread.
    The results of these SQL-Statements are stored in Variables and via INSERT INTO the Information will be stored
    in the Table Pokemon_has_Spread with the specific percentage(chance) of this Spread on this specific Pokemon.
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
    mysecondcursor = mydb.cursor(buffered=True)
    for pokemon in data["data"]:
        mycursor.execute("SELECT poke_id FROM Pokemon WHERE pokemonName = '%s'" %pokemon)
        pokemonid = mycursor.fetchone()
        for spread in data["data"][pokemon]["Spreads"]:
            mysecondcursor.execute("SELECT spread_id FROM Spread WHERE pokemonSpread = '%s'" %spread)
            spreadid = mysecondcursor.fetchone()
            percentage = data["data"][pokemon]["Spreads"][spread]
            mysecondcursor.execute('INSERT INTO Pokemon_has_Spread(poke_id,spread_id,percentage) VALUES (%s,%s,%s)', (pokemonid[0], spreadid[0],percentage))
            mydb.commit()