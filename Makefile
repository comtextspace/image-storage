install:
	poetry install

shell:
	poetry shell

develop:
	 uvicorn main:app --reload