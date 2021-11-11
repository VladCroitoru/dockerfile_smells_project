FROM python:2.7.14-slim-jessie
ENV INITSYSTEM on

RUN apt-get update && apt-get install -y build-essential libffi-dev freetds-dev libpq-dev libmysqlclient-dev python3-dev python3-pip npm nodejs-legacy virtualenv nmap byobu sudo vim && \
       npm install -g configurable-http-proxy && \
       pip install --upgrade pip cython setuptools ipykernel && \
       pip3 install --upgrade pip setuptools cython && \
       mkdir -p /etc/jupyterhub && mkdir -p /data/home
RUN    pip3 install --upgrade notebook jupyterhub jupyterlab oauthenticator && \
       jupyter serverextension enable --py jupyterlab --sys-prefix 
COPY ./jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py
COPY ./sudoers /etc/sudoers

WORKDIR /
EXPOSE 80
CMD jupyterhub --ip '*' --port=80 -f /etc/jupyterhub/jupyterhub_config.py --debug
#CMD sleep infinity
