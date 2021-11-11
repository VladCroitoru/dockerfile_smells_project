FROM python
LABEL org.container.image.authors="grimsleepless@protonmail.com"

ENV POETRY_VERSION=1.1.7

RUN apt update && \
    apt dist-upgrade -y && \
    apt install -y python3-dev curl build-essential python3-pip && \
    pip install poetry==$POETRY_VERSION

WORKDIR /code/

ADD poetry.lock pyproject.toml /code/
RUN cd /code && poetry install --no-interaction --no-ansi

ADD anki_swiss_knife /code/anki_swiss_knife/
ADD Makefile /code/

ENTRYPOINT ["poetry", "run", "python", "anki_swiss_knife/main.py"]
