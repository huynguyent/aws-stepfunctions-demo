
format:
	poetry run black .
	poetry run isort .

test:
	poetry run black --check .
	poetry run isort --check-only .
	poetry run mypy .
