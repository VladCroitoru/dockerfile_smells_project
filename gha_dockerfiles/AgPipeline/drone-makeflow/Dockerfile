FROM ubuntu:20.04 as base
ENV DOCKER_IMAGE agdrone/drone-workflow:1.1
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /

# Install Python
RUN apt-get update -y \
    && apt-get install --no-install-recommends -y \
    git \
    python3.8 \
    python3-pip \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && python3.8 -m pip install -U pip \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Install dependencies
RUN apt-get update -y \
    && apt-get install --no-install-recommends -y \
    software-properties-common \
    wget \
    python3-gdal \
    gdal-bin   \
    libsm6 \
    libxext6 \
    libxrender1 \
    libglib2.0-0 \
    docker.io \
    libgl1-mesa-dev \
    pdal \
    python3-pip \
    pdal \
    python3-venv \
    python3.8-venv \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install global environment to be used by multiple virtual environments
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libgdal-dev \
        gcc \
        g++ \
        python-dev \
        python3-dev \
        python3.8-dev \
        curl && \
    python3.8 -m pip install --upgrade --no-cache-dir \
        wheel && \
    python3.8 -m pip install --upgrade --no-cache-dir \
        influxdb matplotlib Pillow pip piexif python-dateutil pyyaml scipy utm numpy cryptography PDAL==2.3.6 && \
    python3.8 -m pip install --upgrade --no-cache-dir \
        pygdal==3.0.4.* && \
    python3 -m pip install --upgrade --no-cache-dir \
        agpypeline && \
    python3.8 -m pip install --upgrade --no-cache-dir \
        pytest && \
    curl http://ccl.cse.nd.edu/software/files/cctools-7.1.12-source.tar.gz > cctools-source.tar.gz && \
    tar -xzf cctools-source.tar.gz &&\
    cd cctools-*-source && \
    ./configure --prefix /cctools && make install && \
    cd / && rm -r cctools-*-source cctools-source.tar.gz && \
    apt-get remove -y \
        libgdal-dev \
        gcc \
        g++ \
        python-dev \
        python3-dev \
        python3.8-dev \
        curl && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Docker
RUN apt-get update -y && \
    apt-get install -y --reinstall systemd && \
    apt-get remove -y docker docker.io containerd runc && \
    apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable" && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        docker-ce \
        docker-ce-cli \
        containerd.io && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /

FROM base as base_scif
RUN python3.8 -m pip install --upgrade --no-cache-dir scif \
    && echo "Finished install of scif"
ENTRYPOINT ["scif"]

ENV CPLUS_INCLUDE_PATH /usr/include/gdal
ENV C_INCLUDE_PATH /usr/include/gdal

# Install the apps
FROM base_scif as odm_scif
COPY ./scif_app_recipes/opendronemap_v2.2.scif  /opt/
RUN scif install /opt/opendronemap_v2.2.scif

FROM odm_scif as combined_scif
COPY ./scif_app_recipes/ndcctools_v7.1.2_ubuntu20.04.scif  /opt/
COPY ./scif_app_recipes/soilmask_v0.0.1_ubuntu20.04.scif /opt/
RUN scif install /opt/soilmask_v0.0.1_ubuntu20.04.scif
RUN scif install /opt/ndcctools_v7.1.2_ubuntu20.04.scif

COPY ./scif_app_recipes/soilmask_ratio_v0.0.1_ubuntu20.04.scif /opt/
RUN scif install /opt/soilmask_ratio_v0.0.1_ubuntu20.04.scif

COPY ./scif_app_recipes/plotclip_v0.0.1_ubuntu20.04.scif /opt/
RUN scif install /opt/plotclip_v0.0.1_ubuntu20.04.scif

COPY ./scif_app_recipes/canopycover_v0.0.1_ubuntu20.04.scif /opt/
RUN scif install /opt/canopycover_v0.0.1_ubuntu20.04.scif

COPY ./scif_app_recipes/greenness_v0.0.1_ubuntu20.04.scif /opt/
RUN scif install /opt/greenness_v0.0.1_ubuntu20.04.scif

COPY *.jx *.py *.sh jx-args.json /scif/apps/src/
RUN chmod a+x /scif/apps/src/*.sh
RUN chmod a+x /scif/apps/src/*.py

COPY ./scif_app_recipes/git_v0.0.1_ubuntu20.04.scif /opt/
RUN scif install /opt/git_v0.0.1_ubuntu20.04.scif
# Silence a git warning
RUN git config --global advice.detachedHead false

COPY . /home/extractor/drone-makeflow
RUN chmod a+x /home/extractor/drone-makeflow