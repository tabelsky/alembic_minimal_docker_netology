FROM python:3.10
COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

ENTRYPOINT /wait && alembic revision --autogenerate -m 'new migration' && alembic upgrade head
