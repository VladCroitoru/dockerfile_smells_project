FROM python:3.7

WORKDIR /app

COPY Pipfile* ./

RUN pip install pipenv && \
    pipenv install --system --deploy

COPY . .

CMD ./start

EXPOSE 8010
