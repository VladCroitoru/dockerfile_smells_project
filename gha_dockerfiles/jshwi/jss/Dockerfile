# ============================ Environment =============================
FROM python:3.8-slim-buster AS environment

# add user to run entry point under
# set new user's $HOME as WORKDIR
RUN useradd jss
WORKDIR /home/jss

# ensure env variables are set in image
# do not load again when running pipenv
COPY .env .env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1
ENV PIPENV_DONT_LOAD_ENV 1

# =============================== System ===============================
FROM environment AS system

# update and install multi-image system requirements
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-server-dev-all \
    netcat

# ============================== Builder ===============================
FROM system AS builder

# gcc needed for building pysocpg2
RUN apt-get install -y --no-install-recommends gcc

# create python virtual environment to import into other images
COPY Pipfile.lock Pipfile.lock
COPY Pipfile Pipfile
RUN python -m venv .venv
RUN .venv/bin/pip install --upgrade pip pipenv
RUN .venv/bin/pipenv install --deploy --ignore-pipfile

# ================================ Base ================================
FROM system AS base

# import pre-prepared python virtual environment
COPY --from=builder /home/jss/.venv .venv

# copy files over that will be used for production and development
COPY app app
COPY migrations migrations
COPY wsgi.py wsgi.py

# prepare entry point script
COPY scripts/entrypoint.sh entrypoint.sh
COPY scripts/release.sh release.sh
RUN chmod 755 entrypoint.sh

# allow access to server on port 5000
EXPOSE 5000

# ============================= Production =============================
FROM base AS production

# pass ownership of all files to user
RUN chown -R jss:jss ./

# get out of root and run container as user
USER jss

# entry point to ensure database os running and to run command within
ENTRYPOINT ["./entrypoint.sh"]

# ============================ Development =============================
FROM base AS development

# copy development files into image
# they will be needed for editable install
COPY Pipfile.lock Pipfile.lock
COPY Pipfile Pipfile
COPY setup.py setup.py
COPY README.rst README.rst

# install development packages
# # non development install has already been prepared
RUN .venv/bin/pipenv install --deploy --ignore-pipfile --dev

# pass ownership of all files to user
RUN chown -R jss:jss ./

# get out of root and run container as user
USER jss

# entry point to ensure database os running and to run command within
ENTRYPOINT ["./entrypoint.sh"]

# ================================ Nginx ===============================
FROM nginx:1.21.3-alpine as nginx

# replace system-wide nginx configuration with prepared config in this
# repository
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
