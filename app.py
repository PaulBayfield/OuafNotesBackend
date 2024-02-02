from quart import Quart as API

from routes.public.public import construct as RoutePublic

from dotenv import load_dotenv
from os import environ
from datetime import datetime
from aiohttp import ClientSession


load_dotenv(dotenv_path=f".env")


app = API(
    __name__,
)

# App settings
app.config['SERVER_NAME'] = environ["FLASK_SERVER_NAME"]
app.config['SECRET_KEY'] = environ["FLASK_SECRET_KEY"]
app.config['SESSION_COOKIE_DOMAIN'] = f".{environ['FLASK_SERVER_NAME']}"
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 Mb limit
app.config['EXPLAIN_TEMPLATE_LOADING'] = False

app.launch_time = int(datetime.utcnow().timestamp())
app.loaded = False
app.service = environ["SERVICE_URL"]


# Register blueprints
app.register_blueprint(RoutePublic(app))


@app.while_serving
async def lifespan():
    if not app.loaded:
        app.session = ClientSession()
        app.loaded = True

    yield

    if app.loaded:
        await app.session.close()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
