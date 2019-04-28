def fillSpread(databasename):
    """
    This Function will open the specific JSON Pokemon Data File which was choosed by the User / Admin. Based on this Data it's
           going through all Pokemon Spreads in this File. For every Pokemon Spread
           in the JSON FILE there will be a INSERT INTO Statement to fill the Spread Table.
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
        for spread in data["data"][pokemon]["Spreads"]:
            mycursor.execute('INSERT INTO Spread(spread_id,pokemonSpread) VALUES (%s,%s)', (i, spread))
            i = i + 1
            mydb.commit()


