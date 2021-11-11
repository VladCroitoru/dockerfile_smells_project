FROM node:8.9.2

WORKDIR /

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y wget curl vim libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ 

RUN npm install --unsafe-perm -g canvas && \
    apt-get clean

WORKDIR /
