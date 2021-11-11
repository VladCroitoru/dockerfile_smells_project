FROM resero/python-node:p3.6.8-n8.16.0-buster-slim

COPY requirements.txt /tmp/requirements.txt

RUN cd /tmp; \
    pip install --no-cache-dir -r requirements.txt

RUN jupyter serverextension enable --py jupyterlab \
    && jupyter nbextension enable --py widgetsnbextension \
    && jupyter labextension install \
        @jupyter-widgets/jupyterlab-manager \
        jupyter-matplotlib \
        jupyterlab_bokeh \
        @pyviz/jupyterlab_pyviz \
        @jupyterlab/plotly-extension \
        @mflevine/jupyterlab_html

#
# Configure environment
#
# Use 1000 for uid and gid. It's common in the Resero environments for a host directory to be mounted
# into the container, when this is done, it's also common for the uid/gid of the user doing so to be
# 1000. This allows for "correct" file priveledges when doing so
ENV NB_USER=jovyan \
    NB_UID=1000 \
    NB_GID=100

# assumes that the project has been mounted into /home/jovyan/project
# to ensure this derived projects should add the following to their dockerutils.cfg file
# [notebook]
# volumes=--mount type=bind,source={project_root},target=/home/jovyan/project

RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

RUN set -ex; \
    apt-get update; \
    apt-get install -y \
        less \
        vim \
    ; \
    apt-get clean; \
    rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*

COPY root /

CMD ["/usr/local/bin/start-notebook.sh"]
ENTRYPOINT ["/docker-entrypoint.sh"]


#
#  Correctly enabling the UTF-8 en_US encoding
#    (Article: https://daten-und-bass.io/blog/fixing-missing-locale-setting-in-ubuntu-docker-image/)
#
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && apt-get clean \
    && rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

