FROM matthewgall/python-dev:latest

RUN apk add --update \
	postgresql \
	postgresql-dev

WORKDIR /app

COPY . /app
RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt

EXPOSE 5000
CMD ["/env/bin/python", "application.py"]