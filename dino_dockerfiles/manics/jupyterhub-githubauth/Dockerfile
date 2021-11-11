FROM jupyterhub/jupyterhub:0.7.2
MAINTAINER ome-devel@lists.openmicroscopy.org.uk

RUN pip install -U pip
RUN pip install dockerspawner==0.7.0
# TODO: Use upstream pypi release when it's updated
RUN pip install https://github.com/IDR/kubespawner/archive/0.5.2-IDR1.zip
RUN pip install https://github.com/IDR/oauthenticator/archive/0.5.1-IDR2.zip
RUN pip install jupyterhub-dummyauthenticator

RUN useradd user
ADD run.sh /run.sh

ENTRYPOINT ["/run.sh"]
