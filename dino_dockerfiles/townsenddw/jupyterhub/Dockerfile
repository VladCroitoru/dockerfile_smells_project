# Designed to be run as 
# 
# docker run -it -p 8000:8000 jupyterhub/oauthenticator

FROM jupyterhub/jupyterhub:0.7.2

MAINTAINER CSM Data Science Tech Support <dwtownse@calpoly.edu>

# Install oauthenticator, ecsspawner from pip
RUN pip install oauthenticator ecsspawner && \
    rm -rf $PWD ~/.cache

# Create oauthenticator directory and put necessary files in it
WORKDIR /srv/jupyterhub
ENV OAUTHENTICATOR_DIR /srv/jupyterhub
#ADD .aws /root/.aws
ADD jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py
#ADD addusers.sh /srv/jupyterhub/addusers.sh
ADD userlist /srv/jupyterhub/userlist
#ADD ssl /srv/jupyterhub/ssl
RUN chmod 700 /srv/jupyterhub

#RUN ["sh", "/srv/jupyterhub/addusers.sh"]
CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py", "&>>", "/var/log/jupyterhub.log"]
