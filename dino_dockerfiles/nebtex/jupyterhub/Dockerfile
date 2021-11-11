FROM nebtex/python-base:machine-learning
MAINTAINER Nebular Vortex <publicdev@nebtex.com>

RUN mkdir -p /srv/jupyterhub/
ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
WORKDIR /srv/jupyterhub/

EXPOSE 8000

LABEL org.jupyter.service="jupyterhub"

CMD ["jupyterhub", "-f /srv/jupyterhub/jupyterhub_config.py", "--no-ssl"]
