from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BASE_API_URL = "https://www.demonslayer-api.com/api/v1/"

# Helper function for API calls
def fetch_data(endpoint, params=None):
    try:
        response = requests.get(f"{BASE_API_URL}{endpoint}", params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch data"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/characters')
def characters():
    # Display paginated characters
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 5, type=int)
    characters = fetch_data('characters', {'page': page, 'limit': limit})
    return render_template('characters.html', characters=characters.get('content', []), page=page, limit=limit)

@app.route('/characters/<int:character_id>')
def character_detail(character_id):
    # Fetch a specific character by ID
    character_data = fetch_data('characters', {'id': character_id})
    character = character_data.get('content', [])[0] if 'content' in character_data else {}
    return render_template('character_detail.html', character=character)


@app.route('/combat-styles')
def combat_styles():
    # Display paginated combat styles
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 5, type=int)
    combat_styles = fetch_data('combat-styles', {'page': page, 'limit': limit})
    return render_template('combat_styles.html', combat_styles=combat_styles.get('content', []), page=page, limit=limit)

@app.route('/combat-styles/<int:style_id>')
def combat_style_detail(style_id):
    # Fetch a specific combat style by ID
    combat_style_data = fetch_data('combat-styles', {'id': style_id})
    combat_style = combat_style_data.get('content', [])[0] if 'content' in combat_style_data else {}
    return render_template('combat_style_detail.html', combat_style=combat_style)

if __name__ == '__main__':
    app.run(debug=True)
