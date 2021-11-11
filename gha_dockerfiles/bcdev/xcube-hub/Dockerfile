FROM quay.io/bcdev/miniconda3:latest

ARG XCUBE_VIEWER_VERSION=0.4.2
ARG XCUBE_USER_NAME=xcube
ENV XCUBE_HUB_DOCKER_VERSION=2.0.1.dev1
ENV XCUBE_HUB_VERSION=2.0.1.dev1
ENV XCUBE_API_UWSGI_INI_PATH="/home/${XCUBE_USER_NAME}/xcube_hub/resources/uwsgi.yaml"

LABEL maintainer="helge.dzierzon@brockmann-consult.de"
LABEL name="xcube hub service"
LABEL xcube_version=${XCUBE_BASE_VERSION}
LABEL xcube_gen_api_version=${XCUBE_HUB_VERSION}

USER root
SHELL ["/bin/bash", "-c"]
RUN useradd -u 1000 -g 100 -ms /bin/bash ${XCUBE_USER_NAME}
RUN chown -R ${XCUBE_USER_NAME}.users /opt/conda

RUN apt-get -y update --allow-releaseinfo-change
RUN apt-get -y upgrade
RUN apt-get -y install apt-utils
RUN apt-get -y install curl unzip build-essential iputils-ping vim
RUN apt-get -y remove patch
RUN mkdir /var/log/uwsgi && chown 1000.users /var/log/uwsgi

USER ${XCUBE_USER_NAME}

RUN source activate base && conda update -n base conda && conda init
RUN source activate base && conda install -y -c conda-forge mamba

WORKDIR /home/${XCUBE_USER_NAME}
ADD --chown=1000:100 environment.yml environment.yml

RUN mamba env create
RUN echo "conda activate xcube-hub" >> ~/.bashrc

ADD --chown=1000:100 ./ .
RUN source activate xcube-hub && pip install --use-feature=in-tree-build .

EXPOSE 8000
EXPOSE 8080
EXPOSE 5050

CMD ["/opt/conda/envs/xcube-hub/bin/python", "-m", "xcube_hub"]
#CMD ["/bin/bash", "-c", "source activate xcube-hub && uwsgi --yaml ${XCUBE_API_UWSGI_INI_PATH}"]
