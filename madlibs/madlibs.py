"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route("/game")
def show_madlib_form():
    """Give the user a madlib form or say goodbye."""

    answer = request.args.get("game")

    if answer == "no":
        return render_template("goodbye.html")
    else:
        print(answer)
        return render_template("game.html")


@app.route("/madlib")
def show_madlib():
    """Shows madlib results."""

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    gerund_verb = request.args.get("gerund_verb")
    place = request.args.get("place")
    verb = request.args.get("verb")
    adverb = request.args.get("adverb")
    adjective = request.args.get("adjective")
    selection = request.args.get("selection")

    madlibs_template = choice(["madlib.html", "madlib1.html","madlib2.html","madlib3.html"])
    return render_template(madlibs_template, person=person, color=color, noun=noun, 
        gerund_verb=gerund_verb, place=place, verb=verb, adverb= adverb, adjective=adjective, 
        selection=selection)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
