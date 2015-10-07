test:
	tox

flake8:
	flake8 --ignore=E501,F403 --max-complexity 12 tombstones

install:
	python setup.py install

develop:
	python setup.py develop

coverage:
	coverage run --include=tombstones/* -m py.test