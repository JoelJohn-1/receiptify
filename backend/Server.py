import Flask

app = Flask(__name__)


@app.route('/')
def main_route():
    return "HEY"

if __name__ == '__main__':
    app.run()