import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://pokeapi.co/api/v2/pokemon/1'

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}


pokemon_dat = {}
for pokemon in range(1,20,3):
    url = 'https://pokeapi.co/api/v2/pokemon/'+ str(pokemon)
  
    response = requests.get(url, headers = header)
   
    poke_json = response.json()
    
    pokemon_dat[pokemon] = {
        'pokemon_id' :poke_json['id'],
        'pokemon_name': poke_json['name'],
        'pokemon_weight' : poke_json['weight'],
        'pokemon_abilities': poke_json['abilities'],
        'pokemon_base_hp': poke_json['stats'][0]['base_stat']
    }

pokemon_df = pd.DataFrame.from_dict(pokemon_dat).transpose()
#pokemon_df.to_csv('pokemon_details.csv',index= False, header= True)

print(pokemon_df['pokemon_base_hp'])
plt.plot(pokemon_df['pokemon_name'],pokemon_df['pokemon_base_hp']);
plt.show()