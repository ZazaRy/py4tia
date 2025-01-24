from flask import Flask, jsonify, request, redirect

app = Flask(__name__)
fish_count = 0
@app.route("/", methods=["GET"])
def home():
    return f"""
    <html>
    <body>
    <h1>Give Storm a fish!</h1>
    <form method="POST" action="/get_fish">
        <button type=submit name="get_fish">Gimme Gimme Gimme</button>
    </form>
    <pre>{fish_count}</pre>
    </body>
    </html>
    """

@app.route("/get_fish", methods=["POST"])
def get_fish():
    global fish_count
    fish_count += 1
    return redirect("/")







if __name__ == "__main__":
    app.run()
