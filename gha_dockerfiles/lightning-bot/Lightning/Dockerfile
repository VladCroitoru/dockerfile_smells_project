FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1 \
	POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential git libpq-dev \
	&& apt-get clean \
 	&& rm -rf /var/lib/apt/lists/*

WORKDIR /bot

# Poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python


COPY . .

RUN poetry install --no-ansi


CMD ["poetry", "run", "lightning"]