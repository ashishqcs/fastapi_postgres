dev-env:
	alembic upgrade head
	uvicorn app.main:app --reload
