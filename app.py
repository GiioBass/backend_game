from text_adventure_game import create_app
from text_adventure_game.routes.player_routes import player_bp

app = create_app()  # Llama a la función para crear la app

app.register_blueprint(player_bp, url_prefix='/player')

if __name__ == '__main__':
    app.run(debug=True)
