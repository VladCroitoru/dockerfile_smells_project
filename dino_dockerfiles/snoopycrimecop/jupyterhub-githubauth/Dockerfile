FROM jupyterhub/jupyterhub:0.7.2
MAINTAINER ome-devel@lists.openmicroscopy.org.uk

RUN pip install -U pip
RUN pip install dockerspawner==0.7.0
# TODO: Use upstream pypi release when it's updated
RUN pip install https://github.com/IDR/kubespawner/archive/0.5.2-IDR1.zip
RUN pip install https://github.com/IDR/imagespawner/archive/0.1.0-idr.zip
RUN pip install https://github.com/IDR/oauthenticator/archive/0.5.1-IDR3.zip
RUN pip install jupyterhub-dummyauthenticator

ADD https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.7.2/examples/cull-idle/cull_idle_servers.py /srv/jupyterhub/
ADD jupyterhub_config.py /srv/jupyterhub/

RUN useradd user
ADD run.sh /run.sh

ENTRYPOINT ["/run.sh"]
