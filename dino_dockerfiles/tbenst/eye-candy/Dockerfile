FROM node:10.13-stretch
RUN mkdir -p /www/src
RUN mkdir /www/view
WORKDIR /www
# RUN npm install --quiet --production
RUN apt-get update && apt-get -y install \
    ffmpeg \
    libx264-dev
COPY web/package.json /www
COPY web/package-lock.json /www
RUN npm install --quiet
COPY web/src /www/src
COPY web/view /www/view
COPY .git /tmp/
RUN git -C /tmp rev-parse --verify HEAD > /www/git-sha
RUN rm -rf /tmp/.git
