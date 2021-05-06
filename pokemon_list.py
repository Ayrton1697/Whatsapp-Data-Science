import pandas as pd 
import requests 
import matplotlib as plt
import seaborn as sns
#POKEMON LIST
url = 'https://pokeapi.co/api/v2/pokemon/1'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}


pokemon_list = {}
for pokemon in range(1,4):
    url = 'https://pokeapi.co/api/v2/pokemon/'+ str(pokemon)
  
    response = requests.get(url, headers = header)
   
    poke_json = response.json()
    
    pokemon_list[pokemon] = {
        'pokemon_id' :poke_json['id'],
        'pokemon_name': poke_json['name']
    }

pokemon_list_df = pd.DataFrame.from_dict(pokemon_list).transpose()
pokemon_list_df.to_csv('pokemon_list.csv',index= False, header= True)