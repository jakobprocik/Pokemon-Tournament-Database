


def fillMove(databasename):
    """"
    This Function is parsing a specific Website(which will be anonymised). The functions is using BeatifullSoup with the find_all
    Function to find all <a> with the class "ent-name". The function will loop over the results and cut the nonsense of the String out.
    While this function is looping over the results there is a variable i which we use as the move_id.

    """
    from bs4 import BeautifulSoup
    import requests
    import mysql.connector

    url = 'XXXXXX'
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
        tag = tag.lower().replace(" ", "").replace("'", "").replace("-", "")
        mycursor.execute('INSERT INTO Move(move_id,move_Name) VALUES (%s,%s)', (i, tag))
        i = i + 1
        mydb.commit()
