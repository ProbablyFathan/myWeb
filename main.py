from flask import Flask, render_template, jsonify

# __name__ how this file involve
app = Flask(__name__)

catList = [{'name': 'Siamese',
  'origin': 'Thailand',
  'description': 'The Siamese is a popular breed of domestic cat known for its distinctive blue eyes and sleek, slender body.',
  'temperament': ['Active', 'Intelligent', 'Curious'],
  'link': 'https://assets.elanco.com/8e0bf1c2-1ae4-001f-9257-f2be3c683fb1/fca42f04-2474-4302-a238-990c8aebfe8c/Siamese_cat_1110x740.jpg',
  'url': 'siamese'},
 {'name': 'Persian',
  'origin': 'Iran',
  'description': 'The Persian is a long-haired breed of cat with a round face and short muzzle. It is known for its calm and gentle personality.',
  'temperament': ['Calm', 'Gentle', 'Affectionate'],
  'link': 'https://www.omlet.co.uk/images/cache/1024/682/Cat-Persian_Self-A_white_Persian_with_the_long_fluffy_coat_they_are_famous_for.jpg',
  'url': 'persian'},
 {'name': 'Sphynx',
  'origin': 'Canada',
  'description': 'The Sphynx is a hairless breed of cat known for its wrinkled skin and large ears. It is an active and affectionate breed.',
  'temperament': ['Active', 'Affectionate', 'Playful'],
  'link': 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F04%2F08%2Fsphynx-square-standing-553638123.jpg',
  'url': 'sphynx'},
 {'name': 'Bengal',
  'origin': 'United States',
  'description': 'The Bengal is a domestic breed of cat that resembles a small leopard. It is known for its energetic and playful personality.',
  'temperament': ['Energetic', 'Playful', 'Intelligent'],
  'link': 'https://petkeen.com/wp-content/uploads/2022/02/bengal-cat-on-carpet_Elena-Sonmez-Shutterstock.jpg',
  'url': 'bengal'},
 {'name': 'Maine Coon',
  'origin': 'United States',
  'description': 'The Maine Coon is a large, long-haired breed of cat with a gentle and sociable personality. It is known for its love of water.',
  'temperament': ['Gentle', 'Sociable', 'Adaptable'],
  'link': 'https://www.zooplus.co.uk/magazine/wp-content/uploads/2019/03/maine-coon-cat-breed.jpg',
  'url': 'maine-coon'},
 {'name': 'Scottish Fold',
  'origin': 'Scotland',
  'description': 'The Scottish Fold is a breed of cat known for its folded ears and round face. It is a calm and affectionate breed.',
  'temperament': ['Calm', 'Affectionate', 'Playful'],
  'link': 'https://cf.ltkcdn.net/cats/cat-breeds/images/orig/326557-1600x1030-scottish-fold-cat.jpg',
  'url': 'scottish-fold'},
 {'name': 'Russian Blue',
  'origin': 'Russia',
  'description': 'The Russian Blue is a short-haired breed of cat with a distinctive blue-grey coat. It is known for its shy but affectionate personality.',
  'temperament': ['Shy', 'Affectionate', 'Intelligent'],
  'link': 'https://cdns.klimg.com/merdeka.com/i/w/news/2022/01/20/1399358/content_images/670x335/20220120104520-1-russian-cat-001-khulafa-pinta-winastya.jpg',
  'url': 'russian-blue'},
 {'name': 'American Shorthair',
  'origin': 'United States',
  'description': 'The American Shorthair is a medium-sized breed of cat known for its muscular build and easygoing personality.',
  'temperament': ['Easygoing', 'Friendly', 'Adaptable'],
  'link': 'https://www.thesprucepets.com/thmb/8o5e2mkJcAr4kODvsllTf2xiioo=/4778x0/filters:no_upscale():strip_icc()/GettyImages-925319984-36b97d913d934d229d8b0d528a7da64e.jpg',
  'url': 'american-shorthair'},
 {'name': 'Ragdoll',
  'origin': 'United States',
  'description': 'The Ragdoll is a large, long-haired breed of cat with a relaxed and affectionate personality. It is known for its tendency to go limp when picked up.',
  'temperament': ['Relaxed', 'Affectionate', 'Gentle'],
  'link': 'https://assets.elanco.com/8e0bf1c2-1ae4-001f-9257-f2be3c683fb1/ac235c31-8953-4e7e-a582-2d5fa92d60d6/ragdoll_cat_01401.jpg',
  'url': 'ragdoll'},
 {'name': 'Devon Rex',
  'origin': 'England',
  'description': 'The Devon Rex is a curly-haired breed of cat with a playful and affectionate personality. It is known for its large ears and mischievous nature.',
  'temperament': ['Playful', 'Affectionate', 'Mischievous'],
  'link': 'https://cdn.shopify.com/s/files/1/0997/4496/articles/Blue_Eyed_Devon_Rex_Cat_d9234955-823a-459d-8b14-fb1340247c0e_1200x.jpg?v=1588962514',
  'url': 'devon-rex'}]

homeDescription = "The cat (<i>Felis catus</i>) is a domestic species of small carnivorous mammal. It is the only domesticated species in the family <i>Felidae</i> and is commonly referred to as the domestic cat or house cat to distinguish it from the wild members of the family."

@app.route("/")
def mainPage():
  return render_template('home.html', title="Cat Website", description=homeDescription, catList=catList)

@app.route("/api/cats.json")
def catsJson(): return jsonify(catList)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  print('done')

print()