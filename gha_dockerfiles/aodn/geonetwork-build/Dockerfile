FROM ubuntu:16.04

ARG BUILDER_UID=9999

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV HOME /home/builder
ENV JAVA_TOOL_OPTIONS -Duser.home=/home/builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    git-core \
    libxml2-utils \
    libnetcdf11 \
    libgsl2 \
    libudunits2-0 \
    openjdk-8-jdk \
    python3-dev \
    maven \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10

RUN wget -q https://bootstrap.pypa.io/pip/3.5/get-pip.py \
    && python get-pip.py pip==18.1 setuptools==49.6.0 wheel==0.35.1 \
    && rm -rf get-pip.py

RUN pip install \
    bump2version==0.5.10

RUN useradd --create-home --no-log-init --shell /bin/bash --uid $BUILDER_UID builder
USER builder
WORKDIR /home/builder
