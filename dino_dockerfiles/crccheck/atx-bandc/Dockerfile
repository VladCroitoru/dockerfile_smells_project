FROM python:3.8
LABEL maintainer="Chris <c@crccheck.com>"

RUN apt-get update -qq && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
  # For pdfs
  ghostscript imagemagick \
  # For lxml
  libxml2-dev libxslt1-dev \
  libpq-dev \
  > /dev/null && \
  apt-get clean && rm -rf /var/lib/apt/lists/*
# Fix https://bugs.archlinux.org/task/60580
RUN sed -i 's/.*code.*PDF.*//' /etc/ImageMagick-6/policy.xml
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV POETRY_VERSION 1.1.4
RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN POETRY_VIRTUALENVS_IN_PROJECT=true poetry install --no-dev

COPY . /app
EXPOSE 8000
HEALTHCHECK CMD nc -z localhost 8000

CMD [".venv/bin/waitress-serve", "--port=8000", "bandc.wsgi:application"]
