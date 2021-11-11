FROM node:lts-alpine3.14

# Korean Fonts
RUN apk --update add fontconfig
RUN mkdir -p /usr/share/fonts/nanumfont
RUN wget http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip
RUN unzip NanumFont_TTF_ALL.zip -d /usr/share/fonts/nanumfont
RUN fc-cache -f && rm -rf /var/cache/*

# bash install
RUN apk add bash

# Language
ENV LANG=ko_KR.UTF-8 \
    LANGUAGE=ko_KR.UTF-8

# Set the timezone in docker
RUN apk --no-cache add tzdata && \
        cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
        echo "Asia/Seoul" > /etc/timezone

# Create Directory for the Container
WORKDIR /app

COPY ./ ./
RUN npm install

# wait-for-it.sh
# COPY wait-for-it.sh ./
RUN chmod +x wait-for-it.sh

# Docker Demon Port Mapping
EXPOSE 3000

# Node ENV
ENV NODE_ENV=production
ENV NODE_OPTIONS=--max_old_space_size=1024
#ENV DB_HOST postgres
#ENV HOST_PORT 5432
#ENV DB_USER postgres
#ENV DB_PASSWORD super1234
#ENV DB_DATABASE baeum-api