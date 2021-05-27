from flask import render_template, Blueprint

main = Blueprint('main', __name__)

# This is Index Route
@main.route("/")
def index():
	return render_template('index.html')

# This is about Route
@main.route("/game")
def game():
	return render_template('game.html')



# This is about Route
@main.route("/restart_game")
def restart_game():
	return render_template('game.html')