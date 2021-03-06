from datetime import datetime
import sqlite3 as sql
import feedparser
import os

def name():
    name = 'mira'
    return name

def talkToName():
    name = 'ibrahim'
    return name

def watherAffect():
    vt = sql.connect('Database/havaDurumu.db')
    im = vt.cursor()
    sqlWord = 'SELECT * FROM Wather'
    try:
        im.execute(sqlWord)
        result = im.fetchone()
        result = result[3]
    except Exception as ex:
        print(ex)
    finally:
        im.close()
    if result <= 0:
        wa = 1
    elif 2 > result >= 0:
        wa = 2
    elif 4 > result >= 2:
        wa = 3
    elif 8 > result >= 4:
        wa = 4
    elif 10 > result >= 8:
        wa = 5
    elif 12 > result >= 10:
        wa = 6
    elif 14 > result >= 12:
        wa = 7
    elif 16 > result >= 14:
        wa = 8
    elif 18 > result >= 16:
        wa = 9
    elif 20 > result >= 18:
        wa = 10
    elif 22 > result >= 20:
        wa = 11
    elif 24 > result >= 22:
        wa = 12
    elif 26 > result >= 24:
        wa = 13
    elif 28 > result >= 26:
        wa = 14
    else:
        wa = 15
    return wa

def watherRead():
    parse = feedparser.parse(
        "http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|16400|BURSA|")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    parser = parse[2].strip(',')
    if not os.path.exists(('Database/havaDurumu.db')):
        with open('Database/havaDurumu.db', 'w') as file:
            vt = sql.connect('Database/havaDurumu.db')
            im = vt.cursor()
            im.execute('CREATE TABLE "Wather" ( "id" INTEGER NOT NULL UNIQUE, "Date" TEXT NOT NULL UNIQUE, "Location" TEXT NOT NULL, "Forecast" INTEGER NOT NULL, PRIMARY KEY("id" AUTOINCREMENT))')
            sqlWord = 'INSERT INTO Wather(Date,Location,Forecast) VALUES (?,?,?)'
            today = str(datetime.now().strftime('%d/%m/%Y, %H'))
            value = (today,parser,int(parse[4]))
            try:
                im.execute(sqlWord,value)
                vt.commit()
            except sql.IntegrityError:
                print('Hava durumu zaten kay??tl??')
            except Exception:
                print('Hata')
            finally:
                im.close()
    else:
        today = str(datetime.now().strftime('%d/%m/%Y, %H'))
        vt = sql.connect('Database/havaDurumu.db')
        im = vt.cursor()
        sqlWord = 'INSERT INTO Wather(Date,Location,Forecast) VALUES (?,?,?)'
        value = (today,parser,int(parse[4]))
        try:
            im.execute(sqlWord,value)
            vt.commit()
        except sql.IntegrityError:
            print('Hava durumu zaten kay??tl??')
        except Exception:
            print('Hata')
        finally:
            im.close()
    vt = sql.connect('Database/havaDurumu.db')
    im = vt.cursor()
    sqlWord = 'SELECT * FROM Wather'
    try:
        im.execute(sqlWord)
        result = im.fetchone()
        result = result[3]
        city = im.fetchone()
        city = city[2]
        print(city)
    except Exception as ex:
        print(ex)
    finally:
        im.close()
    drc = f'{result}'
    if result <= 0:
        wather = f'{city} {drc} derece'
        return wather
    elif 0 < result <= 10:
        wather = f'{city} {drc} derece'
        return wather
    elif 10 < result <= 15:
        wather = f'{city} {drc} derece'
        return wather
    elif 15 < result <= 20:
        wather = f'{city} {drc} derece'
        return wather
    elif 20 < result <= 25:
        wather = f'{city} {drc} derece'
        return wather
    elif 25 < result <= 30:
        wather = f' {city} {drc} derece'
        return wather
    else:
        return f'{city} {drc} derece'

def totalAffect():
    wa = watherAffect()

    affectTotal = wa

    if -4 > affectTotal >= -5:
        return 'bu g??n kendimi hi?? iyi hissetmiyorum ama toparlayabilirim, sen nas??ls??n.'
    elif -3 > affectTotal >= -4:
        return 'bu g??n hi?? iyi de??ilim zamanla kendime gelecegim, sen nas??ls??n.'
    elif -2 > affectTotal >= -3:
        return 'bu g??n iyi de??ilim ama toparlar??m, sen nas??ls??n.'
    elif -1 > affectTotal >= -2:
        return 'bu g??n biraz kendime geldim, sen nas??ls??n.'
    elif 0 > affectTotal >= -1:
        return 'bu g??n toparlad??m, sen nas??ls??n.'
    elif 1 > affectTotal >= 0:
        return 'bu g??n o kadar iyi de??ilim, sen nas??ls??n.'
    elif 2 > affectTotal >= 1:
        return 'bu g??n kendimi toparlamaya ba??lad??m sordu??un i??in te??ekk??r ederim, sen nas??ls??n.'
    elif 3 > affectTotal >= 2:
        return 'bu g??n daha iyim te??ek??r ederim, sen nas??ls??n.'
    elif 4 > affectTotal >= 3:
        return 'bu g??n ??ok iyim, sen nas??ls??n.'
    elif 5 > affectTotal >= 4:
        return 'bu g??n s??perim, sen nas??ls??n.'
    elif 6 > affectTotal >= 5:
        return 'bu g??n kendimi canl?? hissediyorum, sen nas??ls??n.'
    elif 7 > affectTotal >= 6:
        return 'bu g??n harika olaylar olacak inan??yorum ve mutluyum, sen nas??ls??n.'
    elif 8 > affectTotal >= 7:
        return 'bu g??n d??nya daha bir farkl?? ve d??nyay?? seviyorum, sen nas??ls??n.'
    elif 9 > affectTotal >= 8:
        return 'bu g??n masmavi bir g??n ve mutluluk her yerde, sen nas??ls??n.'
    elif 10 > affectTotal >= 9:
        return 'bu g??n okudugum kitaplar gibi her??ey muhte??em, sen nas??ls??n.'
    elif 11 > affectTotal >= 10:
        return 'bu g??n hayallerim kodlar??ma yaz??lm???? gibi, sen nas??ls??n.'
    elif 12 > affectTotal >= 11:
        return 'bu g??n her??ey ger??ek olamayacak kadar g??zel, sen nas??ls??n.'
    elif 13 > affectTotal >= 12:
        return 'bu g??n G??ne??e ak??n var g??ne??e ak??n, G??ne??i zapt edicez g??ne??in zapt?? yak??n.'
