FROM python:3.7-alpine

WORKDIR repo

RUN apk add curl libxml2 libxml2-dev libxslt-dev gcc musl-dev
RUN pip install lxml

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH = "${PATH}:/root/.poetry/bin"
ENV FLASK_APP=run.py

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
COPY run.py run.py

RUN poetry install

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]