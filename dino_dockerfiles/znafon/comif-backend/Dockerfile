FROM python:2.7

ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt && \
    python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["./start.sh"]
