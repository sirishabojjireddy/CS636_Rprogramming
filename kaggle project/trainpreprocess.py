import csv
import re


##train data set import
traindiclist=[]
with open('train.csv', mode="r") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    for row in reader:
        traindiclist.append(row)
for i in range(0, len(traindiclist), 1):
    traindiclist[i]['id'] = traindiclist[i].pop('\xef\xbb\xbfid')
allfeatures = list(traindiclist[0].keys())
#print(len(traindiclist))
#print(type(traindiclist[1]))
#print(traindiclist[0]['id'])
#print(allfeatures)

movieid = []
for i in range(0,len(traindiclist),1):
    movieid.append(traindiclist[i]['id'])

## genres preprocessing
## genresid (list) store id of each movie's genres
## genresnum (list) # of genres each movie has
## genresdict (dictionary) to store # of occurrence of each language
## genresdict{genres:frequency}
genres=[]
genresid=[]
generesnum = []
generesdict = {}
flaternlist = []
for i in range(0,len(traindiclist),1):
    genres.append(traindiclist[i]['genres'])
    str = genres[i].replace(' ', '')
    match = re.findall('\d+', str)
    genresid.append(match)
    count = len(match)
    generesnum.append(count)
for i in range(0,len(genresid),1):
    tmp = genresid[i]
    flaternlist.extend(tmp)
for i in range(0,len(flaternlist),1):
    tmp = flaternlist[i]
    if tmp in generesdict.keys():
        generesdict[tmp] = generesdict[tmp]+1
    else:
        generesdict[tmp] = 1
#print(genres[0:10])
#print(genresid[0:10])
#print(generesnum[0:10])
#print(generesdict)


## language preprocessing
## dictlan (dictionary) to store # of occurrence of each language
## disclan{language: frequency}
originallanguage = []
for i in range(0,len(traindiclist),1):
    originallanguage.append(traindiclist[i]['original_language'])
#print(originallanguage[1])
dictlan={}
counter = 0
for i in range(0,len(originallanguage),1):
    tmp = originallanguage[i]
    if tmp in dictlan.keys():
        dictlan[tmp] = dictlan[tmp]+1
    else:
        dictlan[tmp] = 1
#print(dictlan)


## production companies
## producompnum (list) number of production companies in each movie
## make dictionary to count number of occurrence for each companies
## companies{id:# of occurrence}
## Possible approach: we could assign the rank for each company based on its frequency
prodcomp = []
prodcompnum = []
companies={}
flaternlist = []
for i in range(0,len(traindiclist),1):
    prodcomp.append(traindiclist[i]['production_companies'])
    str = prodcomp[i].replace(' ', '')
    match = re.findall('\d+', str)
    count = len(match)
    prodcompnum.append(count)
    prodcomp[i] = match
    if((len(prodcomp[i]))) == 0:
        prodcomp[i] = ['NA']
for i in range(0,len(prodcomp),1):
    tmp = prodcomp[i]
    flaternlist.extend(tmp)
for i in range(0,len(flaternlist),1):
    tmp = flaternlist[i]
    if tmp in companies.keys():
        companies[tmp] = companies[tmp]+1
    else:
        companies[tmp] = 1
#print(prodcomp[0:10])
#print(prodcompnum[0:10])

## production countries
## prodcounnum (list) number of production countries
prodcoun = []
prodcounnum = []
for i in range(0,len(traindiclist),1):
    prodcoun.append(traindiclist[i]['production_countries'])
    str = prodcoun[i].replace(' ', '')
    match = re.findall('[A-Z]{2}', str)
    count = len(match)
    prodcoun[i] = match
    prodcounnum.append(count)
    if ((len(prodcoun[i]))) == 0:
        prodcoun[i] = ['NA']
#print(prodcoun[0:10])
#print(prodcounnum[0:10])

## spoken language
## some movies have more than one language
## create list overseastatus with 0 and 1
## 0 for movie with only one language
## 1 for movie with more than one language

spokenlanguage = []
overseastatus = []
for i in range(0,len(traindiclist),1):
    spokenlanguage.append(traindiclist[i]['spoken_languages'])
    str = spokenlanguage[i].replace(' ', '')
    match = re.findall('\'[a-z]{2}\'', str)
    spokenlanguage[i] = match
for i in range(0,len(spokenlanguage),1):
    if len(spokenlanguage[i]) == 1:
        overseastatus.append(0)
    else:
        overseastatus.append(1)
#print(spokenlanguage[0:10])
#print(overseastatus[0:10])


## release date
## original release date in releasdate list
## the release year is taken from each movie and record in releaseyear list
## the month is taken and transformed into quarter form
## JAN, FEB, MAR - 1
## APR, MAY, JUN - 2
## JUL, AUG, SEP - 3
## OCT, NOV, DEC - 4
releasedate = []
releaseyear = []
releasemonth = []
releasequarter = []
quarter = {'1/':1,'2/':1,'3/':1,'4/':2,'5/':2,'6/':2,
           '7/':3,'8/':3,'9/':3,'10/':4,'11/':4,'12/':4}
for i in range(0,len(traindiclist),1):
    releasedate.append(traindiclist[i]['release_date'])
for i in range(0,len(releasedate),1):
    tmp = ''.join(releasedate[i])
    yearmatch = re.findall('[0-9]{2}$',tmp)
    yearmatch = ''.join(yearmatch)
    releaseyear.append(yearmatch)
    monthmatch = re.findall('^[0-9]+/',tmp)
    monthmatch = ''.join(monthmatch)
    releasemonth.append(monthmatch)
for i in range(0,len(releasemonth),1):
    tmp = ''.join(releasemonth[i])
    qnum = quarter[tmp]
    releasequarter.append(qnum)
#print(releasedate[0:10])
#print(releaseyear[0:10])
#print(releasemonth[0:10])
#print(releasequarter[0:10])


## keywords, number of keywords, rank keywords occurrences
## keywordsid (list) store the keywords id
## keywordscount (list) store the number of keywords each movie has
## keylist (list) used to store all id into one flatten list
## keywordsdict (dictionary) store the number of occurrence for each keyword id
## keywordsdict {keywords ID: # of occurrences}
## the code for keywordsdict is commented due to time issue
keywords = []
keywordsid = []
keywordscount = []
keylist = []
keywordsdict={}
for i in range(0,len(traindiclist),1):
    keywords.append(traindiclist[i]['Keywords'])
for i in range(0, len(keywords),1):
    str = keywords[i].replace(' ','')
    match = re.findall('\d+', str)
    keylist.extend(match)
    count = len(match)
    match = ','.join(match)
    keywordsid.append(match)
    keywordscount.append(count)
#for i in range(0,len(keylist),1):
#    tmp = keylist[i]
#    if tmp in keywordsdict.keys():
#        keywordsdict[tmp] = keywordsdict[tmp]+1
#    else:
#        keywordsdict[tmp] = 1
#print(keywordsid[0:10])
#print(keywordscount[0:10])
#print(keylist[0:10])
#print(keywordsdict['917'])


## cast
## castnum (list) make list of number of cast each movie has
## gendercount (List) make list of number of females, males, or unknown in each movie
## actorname (list) store the actor names for each movie (might be used later, such as count occurrence)
cast = []
castnum = []
gendercount = []
genderdict = {'gender:0':0,'gender:1':1,'gender:2':2}
actorname = []

for i in range(0,len(traindiclist),1):
    tmp = traindiclist[i]['cast']
    str = tmp.replace('\'','')
    str = str.replace(' ', '')
    str = str.replace('-','')
    cast.append(str)
for i in range(0,len(cast),1):
    castmatch = re.findall('cast_id:[0-9]+', cast[i])
    gendermatch = re.findall('gender:[0-9]', cast[i])
    ordermatch = re.findall('order:[0-9]+', cast[i])
    actornamematch = re.findall('name:[\w]+', cast[i])
    actornamematch = ','.join(actornamematch)
    actornamematch = actornamematch.replace('name:','')
    actorname.append(actornamematch)
    count = len(castmatch)
    castnum.append(count)
    gender0 = 0
    gender1 = 0
    gender2 = 0
    sublist = []
    for j in range(0,len(gendermatch),1):
        tmp = gendermatch[j]
        if genderdict[tmp] == 0:
            gender0 = gender0+1
        if genderdict[tmp] == 1:
            gender1 = gender1+1
        if genderdict[tmp] == 2:
            gender2 = gender2+1
    sublist.append((gender0,gender1,gender2))
    gendercount.append(sublist)
#print(len(castnum))
#print(castnum[0:10])
#print(len(gendercount))
#print(gendercount[1])
#print(len(actorname))
#print(actorname[0:3])


## crew
## there are too much departments in this feature
## only count number of crew each movie has (store in crewcount)
## count number of females, males, or unknown (store in crewgendercount)
## use the same genderdict that used in cast part
crew = []
crewcount = []
crewgendercount = []
for i in range(0,len(traindiclist),1):
    tmp = traindiclist[i]['crew']
    str = tmp.replace('\'', '')
    str = str.replace(' ', '')
    str = str.replace('-', '')
    crew.append(str)
#print(len(crew))
for i in range(0,len(crew),1):
    gendermatch = re.findall('gender:[0-9]', crew[i])
    count = len(gendermatch)
    crewcount.append(count)
    gender0 = 0
    gender1 = 0
    gender2 = 0
    sublist = []
    for j in range(0,len(gendermatch),1):
        tmp = gendermatch[j]
        if genderdict[tmp] == 0:
            gender0 = gender0+1
        if genderdict[tmp] == 1:
            gender1 = gender1+1
        if genderdict[tmp] == 2:
            gender2 = gender2+1
    sublist.append((gender0,gender1,gender2))
    crewgendercount.append(sublist)
#print(len(crewcount))
#print(crewcount[0:10])
#print(crewgendercount[0])

revenue= []
budget = []
homepage = []
imdbid=[]
popularity = []
runtime = []
tagline = []
for i in range(0, len(traindiclist),1):
    revenue.append(traindiclist[i]['revenue'])
    budget.append(traindiclist[i]["budget"])
    homepage.append(traindiclist[i]['homepage'])
    imdbid.append(traindiclist[i]["imdb_id"])
    popularity.append(traindiclist[i]['popularity'])
    runtime.append(traindiclist[i]['runtime'])
    tagline.append(traindiclist[i]['tagline'])

rows = zip(movieid,generesnum,prodcompnum,prodcoun,prodcounnum,overseastatus,
           releaseyear,releasequarter,keywordscount,
           castnum,gendercount,actorname,crewcount,crewgendercount,revenue,budget,
           homepage,imdbid,popularity,runtime,tagline)
header = ['id','# of genres', '# of production companies','production countries',
          'number of production countries','Oversea Status','release year','release quarter',
          '# of keywords','# of cast','gender distribution for cast', 'actor name','# of crew',
          'gender distribution for crew','revenue','budget','homepage','imdbid','popularity','runtime','tagline']
with open("preprocess.csv",'wb') as f:
    writer = csv.writer(f)
    writer.writerow([i for i in header])
    for row in rows:
        writer.writerow(row)