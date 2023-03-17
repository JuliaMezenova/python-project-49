setup:
	install brain-games brain-even build publish package-install

install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.1-py3-none-any.whl

lint:
	poetry run flake8 brain_games
