.PHONY: install brain-games build publish package-install

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/hexlet_code-1-py3-none-any.whl

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

brain_even:
	poetry run brain-even

brain_calc:
	poetry run brain-calc

brain_nod:
	poetry run brain-nod

brain_progression:
	poetry run brain-progression
