
import pandas as pd
import requests 
from bs4 import BeautifulSoup
import numpy as np
from googletrans import Translator
from google.transliteration import transliterate_text
import json,re

url = 'https://nighthawknews.wordpress.com/2009/10/21/the-100-greatest-directors-of-all-time-the-complete-list/'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'html.parser')

director_data = soup.find('div',attrs={'class':'post-content'})
directors_list = director_data.findAll('a')

director_name_list =[]
born_list =[]
rank_list=[]
score_list = []
feature_film_list = []
best_film_list = []
worst_film_list= []
awards_list = []
died_list=[]
nominations_list = []
awards_notes_list=[]

def translate_to_tamil(value):
	translator = Translator()
	#sinhala_val = mtranslate.translate(value, 'si', 'en')
	tamil_val = translator.translate(value, dest='ta')
	return tamil_val.text

def transliteration(value):
  result = transliterate_text(value, lang_code='ta')
  return result

director_list =[]

for tag in directors_list[3:103]:
  director_meta_data={}

  url = tag['href']
  response = requests.get(url,headers=headers)
  soup = BeautifulSoup(response.content,'html.parser')
  director_data = soup.find('div',attrs={'class':'post-content'})
  director_name = tag.text
  director_meta_data['title'] = director_name + " - " + transliteration(director_name)
  director_meta_data['name'] = director_name

  director_name_list.append(director_name)

  details = director_data.findAll('li')
  born = details[0].text.replace('Born:','').strip()
  director_meta_data['born'] = born[0:4]

  born_list.append(born)
  notes =""
  died = ""
  awards =""
  nominations=""
  next_died = details[1].text.strip()
  
  if next_died.startswith('Died'):
    died = next_died.replace('Died:','').strip()
   

    died_list.append(died)

    rank = details[2].text.replace('Rank:','').strip()
    
    rank_list.append(rank)
    score = details[3].text.replace('Score:','').strip()
    
    score_list.append(score)
    next = details[4].text.strip()
    if next.startswith('Awards'):
      awards = next.replace('Awards:','').strip()
     

      awards_list.append(awards)
      next_nomin = details[5].text.strip()
      if next_nomin.startswith('Nominations'):
        nominations = next_nomin.replace('Nominations:','').strip()
       
        nominations_list.append(nominations)

        next_notes = details[6].text.strip()
        if next_notes.startswith('Awards Note'):
            notes = next_notes.replace('Awards Note:','').strip()
            
            nominations_list.append(notes)

            feature_film = details[7].text.replace('Feature Films:','').strip()
            
            feature_film_list.append(feature_film)

            best_film = details[8].text.replace('Best Film:','').strip()
           
            best_film_list.append(best_film)
            worst_film = details[9].text.replace('Worst Film:','').strip()
            
            worst_film_list.append(worst_film)
        else:
          feature_film = details[6].text.replace('Feature Films:','').strip()
          feature_film_list.append(feature_film)
          best_film = details[7].text.replace('Best Film:','').strip()
          best_film_list.append(best_film)
          worst_film = details[8].text.replace('Worst Film:','').strip()
          worst_film_list.append(worst_film)
      else: 
        feature_film = details[5].text.replace('Feature Films:','').strip()
        feature_film_list.append(feature_film)
        best_film = details[6].text.replace('Best Film:','').strip()
        best_film_list.append(best_film)
        worst_film = details[7].text.replace('Worst Film:','').strip()
        worst_film_list.append(worst_film)
    else:
      feature_film = details[4].text.replace('Feature Films:','').strip()
      feature_film_list.append(feature_film)
      best_film = details[5].text.replace('Best Film:','').strip()
      best_film_list.append(best_film)
      worst_film = details[6].text.replace('Worst Film:','').strip()
      worst_film_list.append(worst_film)
  else:
    rank = details[1].text.replace('Rank:','').strip()
    rank_list.append(rank)
    score = details[2].text.replace('Score:','').strip()
    score_list.append(score)
    next = details[3].text.strip()
    if next.startswith('Awards'):
      awards = next.replace('Awards:','').strip()
      awards_list.append(awards)

      next_nomin = details[4].text.strip()
      if next_nomin.startswith('Nominations'):
        nominations = next_nomin.replace('Nominations','').strip()
        nominations_list.append(nominations)

        next_notes = details[5].text.strip()
        if next_notes.startswith('Awards Note'):
            notes = next_notes.replace('Awards Note:','').strip()
            nominations_list.append(notes),
            feature_film = details[6].text.replace('Feature Films:','').strip()
            feature_film_list.append(feature_film)
            best_film = details[7].text.replace('Best Film:','').strip()
            best_film_list.append(best_film)
            worst_film = details[8].text.replace('Worst Film:','').strip()
            worst_film_list.append(worst_film)
        else:
          feature_film = details[5].text.replace('Feature Films:','').strip()
          feature_film_list.append(feature_film)
          best_film = details[6].text.replace('Best Film:','').strip()
          best_film_list.append(best_film)
          worst_film = details[7].text.replace('Worst Film:','').strip()
          worst_film_list.append(worst_film)
      else: 
        feature_film = details[4].text.replace('Feature Films:','').strip()
        feature_film_list.append(feature_film)
        best_film = details[5].text.replace('Best Film:','').strip()
        best_film_list.append(best_film)
        worst_film = details[6].text.replace('Worst Film:','').strip()
        worst_film_list.append(worst_film)
    else:
      feature_film = details[3].text.replace('Feature Films:','').strip()
      feature_film_list.append(feature_film)
      best_film = details[4].text.replace('Best Film:','').strip()
      best_film_list.append(best_film)
      worst_film = details[5].text.replace('Worst Film:','').strip()
      worst_film_list.append(worst_film)

  director_meta_data['died'] = int(died) if died else ""
  director_meta_data['rank'] = int(rank) if rank else ""
  director_meta_data['score'] = score
  director_meta_data['awards'] = awards if awards else ""
  director_meta_data['nominations'] = nominations if nominations else ""
  director_meta_data['notes'] = notes if notes else ""
  director_meta_data['feature_film'] = feature_film
  director_meta_data['best_film'] = best_film
  director_meta_data['worst_film'] = worst_film

  director_list.append(director_meta_data)


with open ('director-corpus/directors_tamil.json','w+') as f:
		f.write(json.dumps(data))

with open('director-corpus/directors_tamil.json') as json_file:
    data = json.load(json_file)

for d in data:
  if d['score'].strip() == "":
    d['score'] = 0
  d['score'] = float(d['score'])
  if d['feature_film'].strip() == "":
    d['feature_film'] = 0
  d['feature_film'] = int(d['feature_film'])
  if d['died'] == "":
    d['died'] = 0
  else:
    d['died'] = int(d['died'])
  if d['awards'] == "":
    d['awards'] = "No"

for d in data:
  if d['nominations'] == "":
    d['nominations'] = "No"
  if d['awards'] =="":
    d['awards'] ="No"
  if d['notes'] =="":
    d['notes'] ="No"

def translate_values(dict_meta_data):
  tamil_meta_data = {}
  for key in dict_meta_data:
    if isinstance(dict_meta_data[key],int) or isinstance(dict_meta_data[key],float) or key == "title":
      print(key)
      tamil_meta_data[key] = dict_meta_data[key]
    elif key == "awards" or key == "nominations":
      tamil_meta_data['{}_en'.format(key)] = dict_meta_data[key]
      tamil_meta_data['{}_ta'.format(key)] = translate_to_tamil(dict_meta_data[key])
    else:
      tamil_meta_data['{}_en'.format(key)] = dict_meta_data[key]
      tamil_meta_data['{}_ta'.format(key)] = transliteration(dict_meta_data[key])	
  return tamil_meta_data

with open ('directors_tamil.json','w+') as f:
		f.write(json.dumps(director_tamil_list))

director_tamil_list =[]
for doc in data:
  print(doc)
  doc['born'] = int(doc['born'])
  director_tamil_list.append(translate_values(doc))

def create_meta_all():
	dict_all_meta = {}
	list_keys = ['name_en', 'name_ta', 'best_film_en', 'best_film_ta', 'nomintaions_en', 'nominations_ta', 'awards_en', 'awards_ta']
	for i in list_keys :
		dict_all_meta[i] = []

	with open('director-corpus/directors_tamil.json') as f:
		data = json.loads(f.read())

	for items in data:
		for key in items:
			if key in list_keys:
					if items[key] not in dict_all_meta[key]:
						dict_all_meta[key].append(items[key])
	
	with open ('director-corpus/directors_meta_all.json','w+') as f:
		f.write(json.dumps(dict_all_meta))

