from project import app, settings

# Main com Run pra rodar com o python -m
if __name__ == "__main__":
    app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT,
            debug=settings.FLASK_DEBUG)
