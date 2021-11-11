FROM python:3.6-slim

ARG TOKEN_ARG
ARG ENVIRONMENT
ENV TELEGRAM_API_TOKEN $TOKEN_ARG
ENV ENVIRONMENT $ENVIRONMENT

VOLUME /logs /store

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80

WORKDIR bot
CMD ["python", "app.py"]