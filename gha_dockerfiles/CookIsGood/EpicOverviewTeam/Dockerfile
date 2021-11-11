FROM python:3.8

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get -y install postgresql-client

RUN mkdir /app
COPY . /app/
WORKDIR /app

ENV EMAIL=""
ENV PASSWORD=""
ENV ADMIN_EMAIL=""
ENV ADMIN_PASSWORD=""
ENV URL_SAFE=""
ENV SECRET_KEY=""
ENV FLASK_APP=start.py

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "start.py"]


