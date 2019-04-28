




def fillPokemon_hold_Item(databasename):
    """
          This Function will open the specific JSON Pokemon Data File which was choosed by the User / Admin. Based on this Data it's looking
          for the Pokemon and SELECT the pokemon_id from the pokemon table and the  item_id from the Table Item. For every item and Pokemon
          in the JSON FILE there will be a INSERT INTO Statement to fill the Pokemon_hold_Item Table in addition with percentage from the JSON FILE.
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
        mycursor.execute("SELECT poke_id FROM Pokemon WHERE pokemonName = '%s'" %pokemon)
        pokemonid = mycursor.fetchone()
        for item in data["data"][pokemon]["Items"]:
            if item == 'nothing':
                pass
            else:
                print(item)
                mysecondcursor.execute("SELECT item_id FROM Item WHERE item_Name = '%s'" % item)
                itemid = mysecondcursor.fetchone()
                percentage = data["data"][pokemon]["Items"][item]
                mycursor.execute('INSERT INTO Pokemon_hold_Item(poke_id,item_id,percentage) VALUES (%s,%s,%s)',
                                 (pokemonid[0], itemid[0], percentage))
                mydb.commit()