#
# Dockerfile for pfdcm.
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build --build-arg UID=$UID -t local/pfdcm .
#
# In the case of a proxy (located at say 10.41.13.4:3128), do:
#
#    export PROXY="http://10.41.13.4:3128"
#    docker build --build-arg http_proxy=${PROXY} --build-arg UID=$UID -t local/pfdcm .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pfdcm
#
# To pass an env var HOST_IP to the container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pfdcm
#
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

LABEL DEVELOPMENT="                                                        \
    docker run --rm -it                                                    \
    -p 4005:4005 -p 10402:10402 -p 5555:5555 -p 10502:10502 -p 11113:11113 \
    -v $PWD/pfdcm:/app:ro  local/pfdcm /start-reload.sh                    \
"

ENV DEBIAN_FRONTEND=noninteractive


COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt && rm -v /tmp/requirements.txt
RUN pip install https://github.com/msbrogli/rpudb/archive/master.zip
RUN pip install tzlocal
COPY ./pfdcm /app

RUN apt update                              && \
    apt-get install -y apt-transport-https  && \
    apt -y install xinetd                   && \
    apt -y install dcmtk                    && \
    apt -y install vim telnet netcat procps

COPY xinetd_default /etc/default/xinetd

ENV PORT=4005
EXPOSE ${PORT} 10402 10502 5555 11113
