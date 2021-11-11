FROM ubuntu:artful

MAINTAINER Markus Pfeiffer <markus.pfeiffer@st-andrews.ac.uk>

RUN apt-get update -qq \
    && apt-get -qq install -y build-essential m4 libreadline6-dev libncurses5-dev wget unzip libgmp3-dev cmake git python-pip \
                                   automake libtool libzmq3-dev

RUN    adduser --quiet --shell /bin/bash --gecos "GAP user" --uid 1000 --disabled-password gap \
    && chown -R gap:gap /home/gap/ \
    && mkdir -p /home/gap/inst

RUN    cd /home/gap/inst \
    && git clone --depth 1 https://github.com/gap-system/gap.git \
    && cd gap \
    && ./autogen.sh \
    && ./configure --with-gmp=system \
    && make \
    && make bootstrap-pkg-full \
    && chown -R gap:gap /home/gap/inst

USER gap
ENV HOME /home/gap
ENV GAP_HOME /home/gap/inst/gap
ENV PATH ${GAP_HOME}/bin:${PATH}

RUN    pip install notebook jupyterlab_launcher jupyterlab traitlets ipython pandas vdom

ENV PATH /home/gap/.local/bin:${PATH}

RUN    cd /home/gap/inst/gap \
    && cd pkg \
    && ../bin/BuildPackages.sh \
    && git clone https://github.com/gap-packages/uuid.git \
    && git clone https://github.com/gap-packages/crypting.git \
    && rm -rf ZeroMQ* \
    && git clone https://github.com/gap-packages/ZeroMQInterface.git \
    && cd ZeroMQInterface \
    && ./autogen.sh \
    && ./configure \
    && make \
    && cd .. \
    && cd crypting \
    && ./autogen.sh \
    && ./configure \
    && make \
    && cd .. \
    && git clone https://github.com/gap-packages/JupyterKernel.git \
    && cd JupyterKernel \
    && python setup.py install --user \
    && cd .. \
    && git clone https://github.com/gap-packages/anatph \
    && cd .. \
    && cp bin/gap.sh bin/gap

RUN jupyter serverextension enable --py jupyterlab --user

ENV PATH /home/gap/inst/gap/pkg/JupyterKernel/etc/jupyter:${PATH}
ENV JUPYTER_GAP_EXECUTABLE /home/gap/inst/gap/bin/gap.sh

WORKDIR /home/gap

