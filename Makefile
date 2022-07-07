install:
	poetry install

shell:
	poetry shell

develop:
	 uvicorn app.main:app --reload

test:
	pytest