from app import create_app # __init__.py

flask_app = create_app()

if __name__=="__main__":
    flask_app.run(debug=True)

