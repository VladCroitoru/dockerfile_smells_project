FROM python:2.7

LABEL version="0.1"
LABEL maintaner="Sanyam Jain"
LABEL release-date="12/09/2021"

WORKDIR /app

COPY techtrends/ /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN python ./init_db.py

EXPOSE 3111

CMD [ "python", "./app.py" ]