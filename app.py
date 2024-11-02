
from flask import Flask

from text_adventure_game.models.player_model import Player
from text_adventure_game.controllers.player_controller import create_player

app = Flask(__name__)

# Routes

@app.route('/create_player', methods=['POST'])
def create_player_route():
    return create_player()

if __name__ == '__main__':
    app.run(debug=True)
