from text_adventure_game import create_app, db
from text_adventure_game.models.player_model import Player
from text_adventure_game.controllers.player_controller import create_player

app = create_app()  # Llama a la función para crear la app

# Routes
@app.route('/create_player', methods=['POST'])
def create_player_route():
    return create_player()

if __name__ == '__main__':
    app.run(debug=True)
