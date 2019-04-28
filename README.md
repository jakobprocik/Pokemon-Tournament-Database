# Pokemon-Tournament-Database
------------

This is a Script to make a Pokemon Database from the JSON Files from PokemonShowdown.

## Why this “Maker”
Like me, in previous Project, I love to do some calculation and learn the skills to work with big Datasets. I am a huge Pokemon Fan, and maybe, later on, I can build something like a website for example https://pikalytics.com/. 

## Requirements
**-json
-mysql-connector
-requests
-BeautifulSoup4**


## Target Scenario
If you want to build a website like https://pikalytics.com/ and you have no idea how to get the datasets then you could use the  https://www.smogon.com/stats/ website. The website smogon.com provide you with their data in JSON Format.  But if you want to get the whole Data you have to use the CHAOS Directory and the json there looks like this:
{"info":{"team type":null,"cutoff":1630.0,"cutoff deviation":0,"metagame":"gen7zu","number of battles":19547},"data":{"Loudred":{"Moves":{"blizzard":0.0,"overheat":0.0,"extrasensory":0.0,"hypervoice":1.5715779286,"poweruppunch":0.0014221732,"shadowball":0.1756462288,"protect":0.0,"faketears":0.0,"circlethrow":0.0014221732,"earthquake":0.0003729425,"firepunch":0.0010492307,"icebeam":1.5715779286,"return":0.0014221732,"fireblast":1.5715779286,"echoedvoice":1.3959316997,"whirlwind":0.0},"Checks and Counters":{},"Abilities":{"scrappy":1.5730001018},"Teammates":{"Skitty":0.0,"Golem-Alola":1.3718706183,"Chatot":1.2619696629,"Kecleon":0.0187330194,"Taillow":0.0,"Silvally":0.1524347247,"Braixen":-0.0004306874,"Brionne":1.3955991675,"Amaura":-0.0005170451,"Shuckle":1.3445370674,"Muk":-0.1580066176,"Komala":- …………


**So I build this Script for myself to get a Database ready and use for example Django to provide my website with that Information.**



**ER-Diagram**
The script automatically setup a static Database which will look like this:




![dbstructurepic](https://user-images.githubusercontent.com/48180595/56863865-25c5d100-69bc-11e9-8d9c-4a3c8a28b412.png)
