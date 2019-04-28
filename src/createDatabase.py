


def createStructure(databasename):
    """Creating the Basic MySql Structure for the Database
        For further Information look in the res Folder, there is a Model.
    """
    import mysql.connector

    mydb = mysql.connector.connect(
        host="XXX.XXX.XXX.XXX",
        user="XXX",
        passwd="XXX",
        database=databasename)

    mycursor = mydb.cursor()
    """Table Pokemonm"""
    mycursor.execute("CREATE TABLE Pokemon(poke_id INTEGER PRIMARY KEY,pokemonName VARCHAR(30) NOT NULL UNIQUE,rate FLOAT NOT NULL)")
    """Table Teammates"""
    mycursor.execute("CREATE TABLE Teammates(mate_id INTEGER PRIMARY KEY, pokemonName VARCHAR(30) NOT NULL UNIQUE,piclink VARCHAR(15))")
    """Table Pokemon_has_Teammates"""
    mycursor.execute(
        "CREATE TABLE Pokemon_has_Teammates(poke_id INTEGER REFERENCES Pokemon(poke_id),mate_id INTEGER REFERENCES Teammates(mate_id),percantage FLOAT,PRIMARY KEY(poke_id,mate_id))")
    """Table SPREAD"""
    mycursor.execute("CREATE TABLE Spread(spread_id INTEGER PRIMARY KEY,pokemonSpread VARCHAR(40))")
    """Table Pokemon_has_Spread"""
    mycursor.execute(
        "CREATE TABLE Pokemon_has_Spread(spread_id INTEGER REFERENCES Spread(spread_id),poke_id INTEGER REFERENCES Pokemon(poke_id),percentage FLOAT,PRIMARY KEY(spread_id,poke_id))")
    """Table Ability"""
    mycursor.execute("CREATE TABLE Ability(ability_id INTEGER PRIMARY KEY,ability_Name VARCHAR(25))")
    """Table Pokemon_has_Ability"""
    mycursor.execute(
        "CREATE TABLE Pokemon_has_Ability(ability_id INTEGER REFERENCES Ability(ability_id),poke_id INTEGER REFERENCES Pokemon(poke_id),percentage FLOAT,PRIMARY KEY(ability_id,poke_id))")
    """Table Item"""
    mycursor.execute("CREATE TABLE Item(item_id INTEGER PRIMARY KEY,item_Name VARCHAR(20))")
    """Table Pokemon_hold_Item"""
    mycursor.execute(
        "CREATE TABLE Pokemon_hold_Item(item_id INTEGER REFERENCES Item(item_id),poke_id INTEGER REFERENCES Pokemon(poke_id),percentage FLOAT,PRIMARY KEY(item_id,poke_id))")
    """Table Move"""
    mycursor.execute("CREATE TABLE Move(move_id INTEGER PRIMARY KEY,move_Name VARCHAR(20))")
    """Table Pokemon_has_Move"""
    mycursor.execute(
        "CREATE TABLE Pokemon_has_Move(move_id INTEGER REFERENCES Move(move_id),poke_id INTEGER REFERENCES Pokemon(poke_id),percentage FLOAT,PRIMARY KEY(move_id,poke_id))")