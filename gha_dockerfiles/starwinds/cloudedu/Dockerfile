FROM jupyter/datascience-notebook:latest
USER root
RUN apt-get -y install git
RUN cd /home/jovyan/ && git clone https://github.com/starwinds/ktcloud-toolkit
ARG APIKEY 
ARG SECKEY
ENV KTCAPI="${APIKEY}"
ENV KTCSEC="${SECKEY}"
ENV PYTHONPATH "${PYTHONPATH}:./ktcloud-toolkit"
ARG PASSWD
RUN echo "c.NotebookApp.password='${PASSWD}'" >> /home/jovyan/.jupyter/jupyter_notebook_config.py
