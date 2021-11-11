FROM python:3.6-alpine

ADD requirements.txt /usr/src/app/
WORKDIR /usr/src/app/
RUN pip install --no-cache-dir -r ./requirements.txt && \
	pip install --no-cache-dir gunicorn

ENV PYTHONPATH=/usr/src/app/ \
	FLASK_APP=bitsbox.autoapp \
	BITSBOX_CONFIG=/usr/src/app/config.py
EXPOSE 5000

ADD ./ /usr/src/app/
ENTRYPOINT flask db upgrade && \
	gunicorn -w 2 -k gthread -b 0.0.0.0:5000 bitsbox.autoapp:app
