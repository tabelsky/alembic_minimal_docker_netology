import os

PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = int(os.getenv('PG_PORT'))
PG_DB = os.getenv('PG_DB')


print(f'{PG_USER=}')
print(f'{PG_PASSWORD=}')
print(f'{PG_HOST=}')
print(f'{PG_PORT=}')
print(f'{PG_DB=}')
