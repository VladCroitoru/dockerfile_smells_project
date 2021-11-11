FROM python:slim-buster as requirements
RUN mkdir /install
WORKDIR /install
COPY backend/requirements.txt /requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r /requirements.txt
RUN find /install \( -type d -a -name test -o -name tests \) -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) -exec rm -rf '{}' \+

FROM python:slim-buster as app
RUN \
  apt-get update \
  && apt-get install -y libsqlite3-mod-spatialite \
  && rm -rf /var/lib/apt/lists/*
COPY --from=requirements /install /usr/local
COPY backend/app backend/app
COPY frontend/build backend/app/static
WORKDIR /backend
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]
