CREATE TABLE Pokemon(poke_id INTEGER PRIMARY KEY,pokemonName VARCHAR(30) NOT NULL UNIQUE,rate FLOAT NOT NULL);
CREATE TABLE Teammates(mate_id INTEGER PRIMARY KEY, pokemonName VARCHAR(30) NOT NULL UNIQUE);
CREATE TABLE Pokemon_has_Teammates(poke_id INTEGER REFERENCES Pokemon(poke_id),mate_id INTEGER REFERENCES Teammates(mate_id),percantage FLOAT,PRIMARY KEY(poke_id, mate_id));
CREATE TABLE Spread(spread_id INTEGER PRIMARY KEY,pokemonSpread VARCHAR(40));
CREATE TABLE Pokemon_has_Spread(spread_id INTEGER REFERENCES Spread(spread_id),poke_id INTEGER REFERENCES Pokemon(poke_id),percentage FLOAT,PRIMARY KEY(spread_id,poke_id));
CREATE TABLE Ability(ability_id INTEGER PRIMARY KEY,ability_Name VARCHAR(25));
CREATE TABLE Pokemon_has_Ability(ability_id INTEGER REFERENCES Ability(ability_id),poke_id INTEGER REFERENCES Pokemon(poke_id),percentage FLOAT,PRIMARY KEY(ability_id,poke_id));
CREATE TABLE Item(item_id INTEGER PRIMARY KEY,item_Name VARCHAR(20));
CREATE TABLE Pokemon_hold_Item(item_id INTEGER REFERENCES Item(item_id),poke_id INTEGER REFERENCES Pokemon(poke_id),percentage FLOAT,PRIMARY KEY(item_id,poke_id));
CREATE TABLE Move(move_id INTEGER PRIMARY KEY,move_name VARCHAR(20));
CREATE TABLE Pokemon_has_Move(move_id INTEGER REFERENCES Move(move_id),poke_id INTEGER REFERENCES Pokemon(poke_id),percentage FLOAT,PRIMARY KEY(move_id,poke_id));