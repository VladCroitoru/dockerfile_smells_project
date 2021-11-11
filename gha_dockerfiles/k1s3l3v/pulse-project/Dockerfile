FROM python:3.8.10

WORKDIR /usr/src/app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY alembic/ ./alembic/
COPY app/ ./app/

COPY alembic.ini ./alembic.ini
COPY main.py ./main.py

COPY startup.sh ./startup.sh
RUN chmod 777 ./startup.sh && \
    sed -i 's/\r//' ./startup.sh

EXPOSE 5000

CMD ["./startup.sh"]
