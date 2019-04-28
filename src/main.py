from src import fillItemData,createDatabase,fillPokemon_has_SpreadData
from src import fillTeammatesData,fillMoveData,fillAbilityData,fillSpreadData,fillPokemonData,fillTeammates_has_PokemonData,fillPokemon_hold_ItemData,fillPokemon_has_Ability,fillPokemon_has_MoveData
from bs4 import BeautifulSoup
import requests
import mysql.connector

print("How do you wanne name your Database?")
databasename = input()


mydb = mysql.connector.connect(
        host="XXX.XXX.XXX.XXX",
        user="XXX",
        passwd="XXX",
        database=databasename)



link = requests.get("https://www.smogon.com/stats/")
statslinks = BeautifulSoup(link.content,'html.parser')
urllink = []
i = 1
for month in statslinks.find_all('a'):
    month = str(month)
    if len(month)>25:
        month = month.replace('<a href="', '')[0:7]
        urllink.append(month+"/")
        print("Number:"+str(i)+" "+month)
        i+=1

print("Choose the Date you want to create your DB from!")
userinput = int(input())
userlink = requests.get("https://www.smogon.com/stats/"+urllink[userinput-1]+"chaos/")


userstatslink = BeautifulSoup(userlink.content,'html.parser')
jsonfile = []
j = 1
for json in userstatslink.find_all('a'):
    json = str(json)
    if "1760" in json:
        i = json.index('>')+1
        json = json[i:-9]
        print("Number:"+str(j)+" "+json)
        jsonfile.append(json+".json")
        j += 1

print("Choose your Format!")
userinput2 = int(input())
fileoutput = requests.get("https://www.smogon.com/stats/"+urllink[userinput-1]+"chaos/"+jsonfile[userinput2-1],allow_redirects=True)
open('dbdatafile.json',"wb").write(fileoutput.content)


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE %s" %databasename)
createDatabase.createStructure(databasename)
print("Create Database finished")
fillTeammatesData.fillTeammates(databasename)
print("fillTeammates finished")
fillItemData.fillitemdata(databasename)
print("fillItemdata finished")
fillMoveData.fillMove(databasename)
print("fillMove finished")
fillAbilityData.fillAbility(databasename)
print("fillAbilityData finished")
fillSpreadData.fillSpread(databasename)
print("fillSpreadData finished")
fillPokemonData.fillPokemon(databasename)
print("fillPokemonData finished")
fillTeammates_has_PokemonData.fillTeammates_has_Pokemon(databasename)
print("fillTeammates_has_PokemonData finished")
fillPokemon_hold_ItemData.fillPokemon_hold_Item(databasename)
print("fillPokemon_hold_ItemData finished")
fillPokemon_hold_ItemData.fillPokemon_hold_Item(databasename)
print("fillPokemon_has_Ability finished")
fillPokemon_has_MoveData.fillPokemon_has_Move(databasename)
print("fillPokemon_has_MoveData finished")
fillPokemon_has_SpreadData.fillPokemon_has_Spread(databasename)
print("fillPokemon_has_SpreadData finished")
mydb.commit()