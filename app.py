from text_adventure_game import create_app
from text_adventure_game.routes import blueprints
app = create_app()  # Llama a la función para crear la app

for blueprint, url_prefix in blueprints:
    app.register_blueprint(blueprint, url_prefix=url_prefix)

if __name__ == '__main__':
    app.run(debug=True)
