

В [.env](.env) содержаться переменные окружения, которые пробросятся в [docker-compose.yml](docker-compose.yml)

В [docker-compose.yml](docker-compose.yml) в описание каждого сервиса (`db`, `migrate`), есть раздел `enviroment`, 
в котором описаны переменные окружения контейнера.

Например:
```docker
    environment:
      POSTGRES_USER: ${PG_USER}
```
В контейнере создастся переменная окружения `POSTGRES_USER`, в нее подставится значение 
переменной `PG_USER` из [.env](.env)

Или 

```docker
    environment:
      PG_USER: ${PG_USER}
```

В контейнере создастся переменная окружения `PG_USER`, в нее подставится значение 
переменной `PG_USER` из [.env](.env


В `config.py` считываем переменные окружения из контейнера
```python
import os

PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = int(os.getenv('PG_PORT'))
PG_DB = os.getenv('PG_DB')
```

Можем проверить, что переменные считались правильно
```python
print(f'{PG_USER=}')
print(f'{PG_PASSWORD=}')
print(f'{PG_HOST=}')
print(f'{PG_PORT=}')
print(f'{PG_DB=}')
```

Теперь можем их использовать для конфигурирования alembic в [migrate/env.py](migrate/env.py) 
Для начала их нужно, конечно, импортировать
```python
import config as app_config
```
Теперь настраиваем
```python
from alembic import context

config = context.config
config.set_section_option(config.config_ini_section, "PG_HOST", app_config.PG_HOST)
config.set_section_option(config.config_ini_section, "PG_PORT", str(app_config.PG_PORT))
config.set_section_option(config.config_ini_section, "PG_USER", app_config.PG_USER)
config.set_section_option(config.config_ini_section, "PG_PASSWORD", app_config.PG_PASSWORD)
config.set_section_option(config.config_ini_section, "PG_DB", app_config.PG_DB)
```

Теперь в [alembic.ini](alembic.ini) можем прописывать `sqlalchemy.url` используя поля созданные выше
```ini
sqlalchemy.url = postgresql+psycopg2://%(PG_USER)s:%(PG_PASSWORD)s@%(PG_HOST)s:%(PG_PORT)s/%(PG_DB)s
```
