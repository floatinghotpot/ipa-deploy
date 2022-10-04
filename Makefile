
test:
	pytest

version:
	python3 ipa_deploy/version.py bump

clean:
	rm -rf dist/*
	rm -rf build/*

package:
	rm -rf dist/*
	python3 setup.py sdist bdist_wheel
	ls -la dist/

publishtest:
	twine upload --repository testpypi dist/* --verbose

publish:
	twine upload --repository pypi dist/* --verbose
