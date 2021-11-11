# An incomplete base Docker image for running JupyterHub
#
# Add your configuration to create a complete derivative Docker image.
#
# Include your configuration settings by starting with one of two options:
#
# Option 1:
#
# FROM jupyterhub/jupyterhub:latest
#
# And put your configuration file jupyterhub_config.py in /srv/jupyterhub/jupyterhub_config.py.
#
# Option 2:
#
# Or you can create your jupyterhub config and database on the host machine, and mount it with:
#
# docker run -v $PWD:/srv/jupyterhub -t jupyterhub/jupyterhub
#
# NOTE
# If you base on jupyterhub/jupyterhub-onbuild
# your jupyterhub_config.py will be added automatically
# from your docker directory.

FROM ubuntu:14.04 
MAINTAINER Kundaje Lab (forked from Jupyter project) 
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# install nodejs, utf8 locale
#ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y install npm nodejs nodejs-legacy wget locales git node-less 
#    /usr/sbin/update-locale LANG=C.UTF-8 && \
#    locale-gen C.UTF-8 && \
#    apt-get remove -y locales && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*
#ENV LANG C.UTF-8

# install Python with conda
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-4.0.5-Linux-x86_64.sh -O /tmp/miniconda.sh  && \
    echo 'a7bcd0425d8b6688753946b59681572f63c2241aed77bf0ec6de4c5edc5ceeac */tmp/miniconda.sh' | shasum -a 256 -c - && \
    bash /tmp/miniconda.sh -f -b -p /opt/conda && \
    /opt/conda/bin/conda install --yes python=3.5 sqlalchemy tornado jinja2 traitlets requests pip && \
    /opt/conda/bin/pip install --upgrade pip && \
    rm /tmp/miniconda.sh
ENV PATH=/opt/conda/bin:$PATH


# install js dependencies
RUN npm install -g configurable-http-proxy && rm -rf ~/.npm

ADD . /src/jupyterhub
WORKDIR /src/jupyterhub

RUN python setup.py js && pip install . && rm -rf $PWD ~/.cache ~/.npm

RUN pip install notebook

#conda 2 & conda 3 environments 
RUN conda create -n py3 python=3 anaconda
RUN conda create -n py2 python=2 anaconda

# register py2 kernel

RUN source /opt/conda/bin/activate  py2
#RUN ["/bin/bash", "source", "activate", "py2"]
#make sure to install with --user flag to avoid permissions issues 
RUN ipython kernel install --user
RUN source /opt/conda/bin/deactivate 
#RUN ["/bin/bash","source","deactivate"] 

# register py3 kernel 
RUN source /opt/conda/bin/activate py3
#RUN ["/bin/bash", "source", "activate","py3"] 
#make sure to install with --user flag to avoid permissions issues 
RUN ipython kernel install --user 
#install bash kernel 
RUN git clone https://github.com/takluyver/bash_kernel
RUN pip install bash_kernel 
RUN python -m bash_kernel.install 
RUN source /opt/conda/bin/deactivate 
#RUN ["/bin/bash","source","deactivate"] 

RUN mkdir -p /srv/jupyterhub/
WORKDIR /srv/jupyterhub/
EXPOSE 8000

LABEL org.jupyter.service="jupyterhub"

ONBUILD ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py", "--no-ssl", "--port","80"]

