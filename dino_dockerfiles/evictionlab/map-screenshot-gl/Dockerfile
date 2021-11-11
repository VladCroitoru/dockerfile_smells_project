FROM node:6-stretch

ENV NODE_ENV="production"
RUN apt-get -qq update \
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \
    apt-transport-https \
    curl \
    unzip \
    build-essential \
    python \
    libcairo2-dev \
    libgles2-mesa-dev \
    libgbm-dev \
    libllvm3.9 \
    libprotobuf-dev \
    libxxf86vm-dev \
    xvfb \
&& apt-get clean

RUN mkdir -p /usr/src/app
COPY /src /usr/src/app
RUN cd /usr/src/app && npm install --production
ENTRYPOINT ["/usr/src/app/run.sh"]