FROM node:14-buster-slim AS builder
LABEL maintainer="Pouria Hadjibagheri <Pouria.Hadjibagheri@phe.gov.uk>"

WORKDIR /app/static_private

COPY ./app/static_private/           /app/static_private/

WORKDIR /app/static_private/
RUN rm -rf node_modules
RUN npm install
RUN npm rebuild node-sass
RUN npx browserslist@latest --update-db
RUN yarn install
RUN yarn run build
RUN rm -rf node_modules


#FROM node:14-buster-slim AS cms
#LABEL maintainer="Pouria Hadjibagheri <Pouria.Hadjibagheri@phe.gov.uk>"
#
#COPY ./app/static_private/covid19-cms           /app/static_private/covid19-cms
#
#WORKDIR /app/static_private/covid19-cms
#RUN rm -rf node_modules
#RUN npm install
#RUN npm rebuild node-sass
#RUN npx browserslist@latest --update-db
#RUN yarn install
#RUN yarn run build
#RUN rm -rf node_modules


FROM python:3.9-buster
LABEL maintainer="Pouria Hadjibagheri <Pouria.Hadjibagheri@phe.gov.uk>"

# Gunicorn binding port
ENV GUNICORN_PORT 5000

ENV PYTHONPATH            /app/app
ENV CSS_PATH              $PYTHON_PATH/static_private/css
ENV JS_PATH              $PYTHON_PATH/static_private/js
ENV DEFAULT_MODULE_NAME   administration.asgi

# ----------------------------------------------------------------------------------------
# Startup scripts - copied from `./server/startup/`
# ----------------------------------------------------------------------------------------
ENV ENTRYPOINT             entrypoint.sh
ENV START_GUNICORN         start-gunicorn.sh
ENV RELOAD                 start-reload.sh

# ----------------------------------------------------------------------------------------
# Configurations - copied from `./server/config/`
# ----------------------------------------------------------------------------------------
ENV GUNICORN_CONF         gunicorn_conf.py
ENV SUPERVISOR_CONF       supervisord.conf
# Do not include `.py` extension for Uvicorn
ENV UVICORN_CONF          uvicorn_worker

# ----------------------------------------------------------------------------------------
# Supervisor configurations
# ----------------------------------------------------------------------------------------
ENV _RUNTIME_CONF_PATH     /opt
ENV _SUPERVISOR_PATH       $_RUNTIME_CONF_PATH/supervisor
ENV _SUPERVISOR_CONF_FILE  $_SUPERVISOR_PATH/$SUPERVISOR_CONF

# ----------------------------------------------------------------------------------------
# Uvicorn configurations
# ----------------------------------------------------------------------------------------
# Uvicorn worker class
ENV _WORKER_CLASS_NAME     APIUvicornWorker
# Import path
ENV _WORKER_CLASS          $UVICORN_CONF.$_WORKER_CLASS_NAME
ENV _WORKER_CLASS_PATH     $PYTHONPATH/$UVICORN_CONF.py

# ----------------------------------------------------------------------------------------
# Gunicorn config
# ----------------------------------------------------------------------------------------
ENV _GUNICORN_CONF         $_RUNTIME_CONF_PATH/gunicorn/$GUNICORN_CONF
ENV _START_GUNICORN        $_RUNTIME_CONF_PATH/gunicorn/$START_GUNICORN

# ----------------------------------------------------------------------------------------
# Ngnix configurations - copied from `./server/ngnix/`
# ----------------------------------------------------------------------------------------
ENV _NGINX_RUNTIME_NAME   hosts.nginx
ENV _NGINX_BASE_PATH      /etc/nginx
ENV _NGINX_BASE_CONF      $_NGINX_BASE_PATH/conf.d
ENV _NGINX_RUNTIME_CONF   $_RUNTIME_CONF_PATH/nginx/$_NGINX_RUNTIME_NAME

# ----------------------------------------------------------------------------------------
# Installation scripts - copied from `./server/installation/`
# ----------------------------------------------------------------------------------------
ENV _INSTALLATION         $_RUNTIME_CONF_PATH/installation        
ENV _NGINX_INSTALLATION   $_INSTALLATION/install-nginx.sh

# ----------------------------------------------------------------------------------------
# Prestart scripts - copied from `./server/prestart/`
# ----------------------------------------------------------------------------------------
ENV PRESTART_INITIATOR     prestart.sh

ENV _CUSTOM_PRESTART_PATH  $_RUNTIME_CONF_PATH/prestart
ENV _PRESTART_SCRIPT       $_CUSTOM_PRESTART_PATH/$PRESTART_INITIATOR

# Updating the OS + installing supervisor
RUN apt-get update                                                   && \
    apt-get upgrade -y --no-install-recommends --no-install-suggests && \
    apt-get install -qy build-essential --no-install-recommends      && \
    apt-get install -y --no-install-recommends supervisor            && \
    rm -rf /var/lib/apt/lists/*

# Installing Nginx
COPY server/installation/install-nginx.sh   $_NGINX_INSTALLATION

RUN bash $_NGINX_INSTALLATION             && \
    rm /etc/nginx/conf.d/default.conf

# Installing Python requirements
COPY ./requirements.txt                     $_INSTALLATION/requirements.txt

RUN python3 -m pip install --no-cache-dir -U pip                                && \
    python3 -m pip install --no-cache-dir setuptools                            && \
    python3 -m pip install -U --no-cache-dir -r $_INSTALLATION/requirements.txt

# Nginx configurations
COPY server/nginx/base.nginx                $_NGINX_BASE_PATH/nginx.conf
COPY server/nginx/upload.nginx              $_NGINX_BASE_CONF/upload.conf
COPY server/nginx/engine.nginx              $_NGINX_BASE_CONF/engine.conf
COPY server/nginx/hosts.nginx               $_NGINX_RUNTIME_CONF

# Gunicorn configurations
COPY server/config/$GUNICORN_CONF           $_GUNICORN_CONF
COPY server/startup/start-gunicorn.sh       $_START_GUNICORN

# Supervisor configurations
COPY server/config/$SUPERVISOR_CONF         $_SUPERVISOR_CONF_FILE

# Main service entrypoint - launches supervisord
COPY server/startup/entrypoint.sh           $_RUNTIME_CONF_PATH/$ENTRYPOINT

# Launch scripts
COPY server/prestart/                       $_CUSTOM_PRESTART_PATH/
RUN mkdir -p /app/app

RUN mkdir -p /run/supervisord/                      && \
    mkdir -p $_RUNTIME_CONF_PATH/log/               && \
    mkdir -p $_RUNTIME_CONF_PATH/gunicorn/          && \
    mkdir -p $_RUNTIME_CONF_PATH/nginx/cache/

RUN rm -rf $_INSTALLATION

# Copying built styles
COPY app/                                      $PYTHONPATH/
COPY --from=builder /app/static_private/css    $CSS_PATH
COPY --from=builder /app/static_private/js     $JS_PATH
COPY server/config/uvicorn_worker.py           $_WORKER_CLASS_PATH

#COPY --from=cms /app/static_private/covid19-cms/build  /app/frontend
#USER app

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-c", "opt/gunicorn/gunicorn_conf.py", "administration.wsgi:app"]