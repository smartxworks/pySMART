build:
	python setup.py bdist_wheel --universal
	python setup.py sdist
upload:
	twine upload dist/*.whl
	twine upload dist/*.tar.gz
