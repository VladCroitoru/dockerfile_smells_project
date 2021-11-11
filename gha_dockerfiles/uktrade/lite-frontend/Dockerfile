FROM python:3.7-slim
WORKDIR /app
RUN apt-get update --fix-missing
RUN apt-get install -y gcc \
  build-essential python3-dev
RUN pip3 install pipenv
ADD Pipfile* /app/
RUN pipenv install --dev --system --deploy
ADD . /app
