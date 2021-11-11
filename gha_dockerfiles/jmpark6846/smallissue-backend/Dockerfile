FROM python:3
ENV PYTHONUNBUFFERED=1
COPY Pipfile /app/
COPY . /app/
WORKDIR /app

RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 8000