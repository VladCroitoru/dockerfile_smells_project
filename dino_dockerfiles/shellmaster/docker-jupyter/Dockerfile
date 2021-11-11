FROM debian:jessie

MAINTAINER Rafal S. <rafal@maracje.pl>

ENV DEBIAN_FRONTEND noninteractive
ENV url="/"
ENV origin="http://127.0.0.1"

RUN apt-get update && apt-get -y install libzmq3-dev && \
apt-get -y install python3-pip && \
pip3 install jupyter && \
# install all extra kernels
# bash
pip3 install bash_kernel && \
python3 -m bash_kernel.install && \
#
rm -rf -- /var/lib/apt/* /var/log/*

COPY jup-stop /bin/jup-stop

VOLUME ["/notebook"]
WORKDIR /notebook

EXPOSE 8080

CMD jupyter-notebook --port 8080 --transport tcp --ip 0.0.0.0 --KernelManager.autorestart=False --NotebookApp.allow_credentials=False --NotebookApp.base_url="${url}" --NotebookApp.allow_origin="${origin}"
