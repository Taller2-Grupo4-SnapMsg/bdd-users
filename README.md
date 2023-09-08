# prueba-fly.io

Para hacer una migración de la base de datos:

alembic revision --autogenerate -m "motivo de la migración"

Para aplicar la migracion:

alembic upgrade head


