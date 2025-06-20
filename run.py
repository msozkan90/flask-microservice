import os
from dotenv import load_dotenv
from app.main import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "False") == "True"
    port = int(os.getenv("FLASK_PORT", 5050))
    app.run(debug=debug, host="0.0.0.0", port=port)
