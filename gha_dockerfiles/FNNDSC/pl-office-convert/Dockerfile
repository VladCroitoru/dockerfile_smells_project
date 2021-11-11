FROM docker.io/python:3.9.1-slim-buster

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="Office File Converter" \
      org.opencontainers.image.description="Convert Excel and ODS spreadsheets to plaintext CSV files."

WORKDIR /usr/local/src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

CMD ["office_convert", "--help"]
