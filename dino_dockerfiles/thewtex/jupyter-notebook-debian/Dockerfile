FROM debian:8
MAINTAINER Matt McCormick <matt.mccormick@kitware.com>

RUN apt-get update && apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get update && apt-get install -y \
  libcurl4-openssl-dev \
  libpython3-dev \
  libsqlite3-dev \
  libzmq3-dev \
  locales \
  git \
  nodejs \
  pandoc \
  python3 \
  python3-pip \
  python3-sphinx \
  sqlite3 \
  sudo \
  zlib1g-dev

RUN pip3 install --upgrade setuptools pip

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
  locale-gen
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN mkdir -p /srv/
WORKDIR /srv/
ENV IPYKERNEL_VERSION 4.4.1
RUN git clone --depth 1 --branch ${IPYKERNEL_VERSION} https://github.com/ipython/ipykernel /srv/ipykernel
WORKDIR /srv/ipykernel
RUN pip3 install .

WORKDIR /srv/
ENV NOTEBOOK_VERSION 4.2.2
RUN git clone --depth 1 --branch ${NOTEBOOK_VERSION} https://github.com/jupyter/notebook /srv/notebook
WORKDIR /srv/notebook/
RUN chmod -R +rX /srv/notebook && \
  pip3 install . && \
  python3 -m ipykernel.kernelspec

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
ENV TINI_VERSION v0.10.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

# Run jupyter as a non-root user, jovyan, by Jupyter project convention.
RUN echo "jovyan ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/notebook && \
  useradd -m -s /bin/bash jovyan && \
  chown -R jovyan:users /home/jovyan
ENV HOME /home/jovyan
ENV SHELL /bin/bash
ENV USER jovyan
USER jovyan
RUN mkdir /home/jovyan/notebooks
WORKDIR /home/jovyan/notebooks

EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]
