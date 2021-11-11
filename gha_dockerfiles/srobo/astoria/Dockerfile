FROM python:3.9-slim as base

WORKDIR /app

RUN pip install dephell[full]

COPY docker/astoria.toml /etc/
COPY astoria/ /app/astoria
COPY pyproject.toml README.md /app/

RUN dephell deps convert --from pyproject.toml --to setup.py

RUN pip install .