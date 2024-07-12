.PHONY: install brain-games build publish package-install

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/hexlet_code-1-py3-none-any.whl

lint:
	poetry run flake8 brain_games
