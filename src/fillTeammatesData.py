def findpicforTeammates():
    """
    This function is scraping links from a Website and building a link to the Picture of the Pokemon.
    These Pictures will be stored in the src/pics.
    :return:
    """
    from bs4 import BeautifulSoup
    import requests
    url = 'XXXXXXXX'
    r = requests.get(url)
    standardurl = "XXXXXXXXX"
    r = r.text
    soup = BeautifulSoup(r, 'html.parser')
    counter = 1
    for link in soup.find_all('img'):
        i = 'Pokémon-Icon'
        link = str(link)
        if i in link:
            anfangsindex = link.index('/')
            link = link[anfangsindex:]
            endeindex = link.index('"')
            link = link[:endeindex]
            fertigerlink = standardurl + link
            pic = requests.get(fertigerlink)
            open('pics/%s.png' % counter, 'wb').write(pic.content)
            counter = counter + 1


def fillTeammates(databasename):
    """This function will fill the Teammates Table in our SQL-Server
     It's Scraping all the Data from a Pokemon Website and looping through them to create a INSERT Statement to fill the Teammates Table.
     The function works with the findpicforTeammates function to store a link for every Pokemon Picture in our Database.
     """
    from bs4 import BeautifulSoup
    import requests
    import mysql.connector
    url = 'XXXXXXXXXXXXXXX'
    r = requests.get(url)
    r = r.text
    soup = BeautifulSoup(r, 'html.parser')
    i = 1
    mydb = mysql.connector.connect(
        host="XXX.XXX.XXX.XXX",
        user="XXX",
        passwd="XXX",
        database=databasename)
    mycursor = mydb.cursor()
    for tag in soup.find_all('a',class_="ent-name"):
        tag = str(tag)
        anfang = tag.find(">")
        tag = tag[anfang+1:len(tag)].replace('</a>',"")
        tag = tag.replace("'", "").replace("'","")
        findpicforTeammates()
        link = 'pics/%s.png' %i
        mycursor.execute('INSERT INTO Teammates(mate_id,pokemonName,piclink) VALUES (%s,%s,%s)',(i,tag,link))
        i = i +1
        mydb.commit()


