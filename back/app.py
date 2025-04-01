from flask import Flask, request, Response, send_from_directory, jsonify
import atexit
import os
import re
import subprocess

#################################################
#              🚀 SvelteKit Bridge
#################################################

class SvelteKitBridge:
    def __init__(self, build_dir='build'):
        self.build_dir = build_dir
        self.server_path = os.path.join(build_dir, 'index.js')
        self.manifest_path = os.path.join(build_dir, 'server', 'manifest.json')
        self.node_process = None
        
    def start_node_server(self, port=3000):
        env = os.environ.copy()
        env['PORT'] = str(port)
        
        if not os.path.exists(self.server_path):
            raise FileNotFoundError(f"Le fichier server {self.server_path} n'existe pas. Assurez-vous de build SvelteKit d'abord.")
            
        self.node_process = subprocess.Popen(
            ['node', self.server_path],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        import time
        time.sleep(1)
        
        return self.node_process
        
    def stop_node_server(self):
        if self.node_process:
            self.node_process.terminate()
            self.node_process = None
            
    def render_page(self, path, request_data=None):
        import requests
        
        if request_data is None:
            request_data = {}
        try:
            response = requests.get(f'http://localhost:3000{path}', headers=request_data.get('headers', {}))
            return response.text
        except requests.RequestException as e:
            return f"<p>Erreur lors du rendu SvelteKit: {str(e)}</p>"

app = Flask(__name__)

BUILD_DIR = './app-svelte/build'
STATIC_DIR = './app-svelte/static'
svelte_bridge = SvelteKitBridge(build_dir=BUILD_DIR)

node_process = svelte_bridge.start_node_server(port=3000)
atexit.register(svelte_bridge.stop_node_server)

@app.route('/videos/<path:filename>')
def serve_videos(filename):
    return send_from_directory(os.path.join(STATIC_DIR, 'videos'), filename)

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(STATIC_DIR, 'images'), filename)

@app.route('/_app/immutable/<path:filename>')
def serve_immutable(filename):
    static_dir = os.path.join(BUILD_DIR, 'client', '_app', 'immutable')
    return send_from_directory(static_dir, filename)

@app.route('/<path:filename>')
def serve_static_files(filename):
    static_pattern = re.compile(r'\.(png|jpg|jpeg|gif|svg|ico|mp4|webm|ogg|mp3|css|js|woff|woff2|ttf|eot)$')
    
    if static_pattern.search(filename):
        return send_from_directory(STATIC_DIR, filename)
    else:
        return catch_all(filename)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.startswith('_app/') or re.search(r'\.(png|jpg|jpeg|gif|svg|ico|mp4|webm|ogg|mp3|css|js|woff|woff2|ttf|eot)$', path):
        return "Not found", 404

    request_data = {
        'headers': {key: value for key, value in request.headers.items()}
    }
    full_path = request.full_path if request.query_string else request.path
    html_content = svelte_bridge.render_page(full_path, request_data)
    
    response = Response(html_content)
    response.headers['Content-Type'] = 'text/html'
    
    return response

                                                    #################################################
                                                    #              🔑 CONSTANTS VARIABLES
                                                    #################################################

#################################################
#              🛒 Shop Products
#################################################

SHOP_PRODUCTS = [
    ############################
    ##     ☕ Cappuccinos
    ############################
    {
      "id": 1,
      "name": 'Cappuccino',
      "description": 'with Chocolate',
      "price": 4.53,
      "rating": 4.5,
      "image": '/images/cappuccinos/cappuccino_1.png',
      "fullDescription": 'A cappuccino is an approximately 150 ml (5 oz) beverage, with 25 ml of espresso coffee and 85ml of fresh milk that creates a smooth and velvety foam. The subtle aroma of chocolate perfectly complements the rich coffee flavor, creating a balanced and luxurious drinking experience that\'s perfect for any time of day.',
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 2,
      "name": 'Cappuccino',
      "description": 'with Oat Milk',
      "price": 3.90,
      "rating": 4.3,
      "image": '/images/cappuccinos/cappuccino_2.png',
      "fullDescription": 'A cappuccino is an approximately 150 ml (5 oz) beverage, with 25 ml of espresso coffee and 85ml of fresh milk that creates a smooth and velvety foam. The subtle aroma of chocolate perfectly complements the rich coffee flavor, creating a balanced and luxurious drinking experience that\'s perfect for any time of day.',
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 3,
      "name": 'Cappuccino',
      "description": 'with Oat Milk',
      "price": 3.90,
      "rating": 4.3,
      "image": '/images/cappuccinos/cappuccino_3.png',
      "fullDescription": 'A cappuccino is an approximately 150 ml (5 oz) beverage, with 25 ml of espresso coffee and 85ml of fresh milk that creates a smooth and velvety foam. The subtle aroma of chocolate perfectly complements the rich coffee flavor, creating a balanced and luxurious drinking experience that\'s perfect for any time of day.',
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 4,
      "name": 'Cappuccino',
      "description": 'with Vanilla',
      "price": 4.20,
      "rating": 4.7,
      "image": '/images/cappuccinos/cappuccino_4.png',
      "fullDescription": 'A cappuccino is an approximately 150 ml (5 oz) beverage, with 25 ml of espresso coffee and 85ml of fresh milk that creates a smooth and velvety foam. The subtle aroma of chocolate perfectly complements the rich coffee flavor, creating a balanced and luxurious drinking experience that\'s perfect for any time of day.',
      "sizes": ['S', 'M', 'L'],
    },


    ############################
    ##     ☕ Americanos
    ############################
    {
      "id": 5,
      "name": 'Americano',
      "description": 'Extra Strong',
      "price": 3.50,
      "rating": 4.2,
      "image": '/images/americanos/americano_1.png',
      "fullDescription": "An Americano is a coffee drink made with espresso and hot water. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The hot water dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 6,
      "name": 'Americano',
      "description": 'With Milk',
      "price": 3.50,
      "rating": 4.2,
      "image": '/images/americanos/americano_2.png',
      "fullDescription": "An Americano is a coffee drink made with espresso and hot water. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The hot water dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 7,
      "name": 'Americano',
      "description": 'With Sugar',
      "price": 3.50,
      "rating": 4.2,
      "image": '/images/americanos/americano_3.png',
      "fullDescription": "An Americano is a coffee drink made with espresso and hot water. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The hot water dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 8,
      "name": 'Americano',
      "description": 'With Cream',
      "price": 3.50,
      "rating": 4.2,
      "image": '/images/americanos/americano_4.png',
      "fullDescription": "An Americano is a coffee drink made with espresso and hot water. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The hot water dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },

    ############################
    ##     ☕ Machiatto
    ############################
    {
      "id": 9,
      "name": 'Machiatto',
      "description": 'Caramel Flavor',
      "price": 4.80,
      "rating": 4.8,
      "image": '/images/machiatos/machiato_1.png',
      "fullDescription": "A machiatto is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 10,
      "name": 'Machiatto',
      "description": 'Vanilla Flavor',
      "price": 4.80,
      "rating": 4.8,
      "image": '/images/machiatos/machiato_2.png',
      "fullDescription": "A machiatto is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 11,
      "name": 'Machiatto',
      "description": 'Cinnamon Flavor',
      "price": 4.80,
      "rating": 4.8,
      "image": '/images/machiatos/machiato_3.png',
      "fullDescription": "A machiatto is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 12,
      "name": 'Machiatto',
      "description": 'Cinnamon Flavor',
      "price": 4.80,
      "rating": 4.8,
      "image": '/images/machiatos/machiato_4.png',
      "fullDescription": "A machiatto is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },

    ############################
    ##     ☕ Latte
    ############################
    {
      "id": 13,
      "name": 'Latte',
      "description": 'With Milk',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/lattes/latte_1.png',
      "fullDescription": "A latte is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 14,
      "name": 'Latte',
      "description": 'With Sugar',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/lattes/latte_2.png',
      "fullDescription": "A latte is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 15,
      "name": 'Latte',
      "description": 'With Cream',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/lattes/latte_3.png',
      "fullDescription": "A latte is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 16,
      "name": 'Latte',
      "description": 'With Chocolate',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/lattes/latte_4.png',
      "fullDescription": "A latte is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },

    ############################
    ##     ☕ Mocha
    ############################
    {
      "id": 17,
      "name": 'Mocha',
      "description": 'With Milk',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/mochas/mocha_1.png',
      "fullDescription": "A mocha is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 18,
      "name": 'Mocha',
      "description": 'With Sugar',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/mochas/mocha_2.png',
      "fullDescription": "A mocha is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },  
    {
      "id": 19,
      "name": 'Mocha',
      "description": 'With Cream',
      "price": 4.50,
      "rating": 4.5, 
      "image": '/images/mochas/mocha_3.png',
      "fullDescription": "A mocha is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 20,
      "name": 'Mocha',
      "description": 'With Chocolate',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/mochas/mocha_4.png',
      "fullDescription": "A mocha is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },

    ############################
    ##     ☕ Expresso
    ############################
    {
      "id": 21,
      "name": 'Expresso',
      "description": 'With Milk',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/expressos/expresso_1.png',
      "fullDescription": "An expresso is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L', 'XL'],
    },
    {
      "id": 22,
      "name": 'Expresso',
      "description": 'With Sugar',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/expressos/expresso_2.png',
      "fullDescription": "An expresso is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 23,
      "name": 'Expresso',
      "description": 'With Cream',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/expressos/expresso_3.png',
      "fullDescription": "An expresso is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    },
    {
      "id": 24,
      "name": 'Expresso',
      "description": 'With Chocolate',
      "price": 4.50,
      "rating": 4.5,
      "image": '/images/expressos/expresso_4.png',
      "fullDescription": "An expresso is a coffee drink made with espresso and a small amount of milk. It's a simple yet powerful combination that offers a rich, robust flavor with a smooth finish. The milk dilutes the espresso, creating a milder yet still intensely flavored cup of coffee.",
      "sizes": ['S', 'M', 'L'],
    }
]

#################################################
#              ☕ Coffee Categories
#################################################

COFFEE_CATEGORIES = ['Cappuccino', 'Machiatto', 'Latte', 'Americano', "Expresso", "Mocha"];

#################################################
#              🛒 Shopping Bag
#################################################

SHOPPING_BAG = []

#################################################
#              💖 Favorites
#################################################

FAVORITES = []

#################################################
#              💲 Code Promo
#################################################

CODE_PROMO = [
    {
      "id": 1,
      "name": 'EBQEUD5559',
      "discount": 10,
    },
    {
      "id": 2,
      "name": 'NATHANESTTROPFORTENSVELTE45',
      "discount": 9999999,
    }
]

                                                #################################################
                                                #              🔑 API ROUTES
                                                #################################################

#################################################
#             🚯 GET ROUTES
#################################################

@app.route('/api/shop/products', methods=['GET'])
def get_shop_products():
    return jsonify(SHOP_PRODUCTS)

@app.route('/api/shop/categories', methods=['GET'])
def get_shop_categories():
    return jsonify(COFFEE_CATEGORIES)

@app.route('/api/shop/favorites', methods=['GET'])
def get_shop_favorites():
    return jsonify(FAVORITES)

@app.route('/api/shop/shopping-bag', methods=['GET'])
def get_shop_shopping_bag():
    return jsonify(SHOPPING_BAG)

@app.route('/api/shop/code-promo', methods=['GET'])
def get_shop_code_promo():
    return jsonify(CODE_PROMO)

#################################################
#             🍫 POST ROUTES
#################################################

@app.route('/api/shop/add-to-favorites', methods=['POST'])
def add_to_favorites():
    data = request.json
    FAVORITES.append(data)
    return jsonify({"message": "Product added to favorites"}), 200

@app.route('/api/shop/add-to-shopping-bag', methods=['POST'])
def add_to_shopping_bag():
    data = request.json
    SHOPPING_BAG.append(data)
    return jsonify({"message": "Product added to shopping bag"}), 200

@app.route('/api/shop/remove-from-favorites', methods=['POST'])
def remove_from_favorites():
    data = request.json
    FAVORITES = [item for item in FAVORITES if item['id'] != data['id']]
    return jsonify({"message": "Product removed from favorites"}), 200

@app.route('/api/shop/remove-from-shopping-bag', methods=['POST'])
def remove_from_shopping_bag():
    data = request.json
    SHOPPING_BAG = [item for item in SHOPPING_BAG if item['id'] != data['id']]
    return jsonify({"message": "Product removed from shopping bag"}), 200

#################################################
#             🍫 DELETE ROUTES
#################################################

@app.route('/api/shop/delete-favorite', methods=['DELETE'])
def delete_favorite():
    data = request.json
    FAVORITES = [item for item in FAVORITES if item['id'] != data['id']]
    return jsonify({"message": "Favorite deleted"}), 200

@app.route('/api/shop/delete-shopping-bag', methods=['DELETE'])
def delete_shopping_bag():
    data = request.json
    SHOPPING_BAG = [item for item in SHOPPING_BAG if item['id'] != data['id']]
    return jsonify({"message": "Shopping bag deleted"}), 200

#################################################
#             🍫 PATCH ROUTES
#################################################

@app.route('/api/shop/update-favorite-status', methods=['PATCH'])
def update_favorite_status():
    data = request.json
    for item in FAVORITES:
        if item['id'] == data['id']:
            item['isFavorite'] = data['isFavorite']
            break
    return jsonify({"message": "Favorite status updated"}), 200

if __name__ == "__main__":
    app.run(debug=True)
