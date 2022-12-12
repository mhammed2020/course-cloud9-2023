install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb
	
	python -m pytest test_samble.py


lint:
	pylint --disable=R,C hello.py

all: install lint test