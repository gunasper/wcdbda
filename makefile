run:
	env FLASK_APP=app.py env FLASK_DEBUG=1 flask run

deps:
	python3 -m pip install -r requirements --user