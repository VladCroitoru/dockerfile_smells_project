#python3 scrapy
FROM python:3.6-alpine
LABEL cn.crotondata.docker.project="spiders"
#RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/main" > /etc/apk/repositories
RUN apk add --update --no-cache \ 
    gcc \
    tzdata \
    openssl-dev \
    libxml2 \
    libxml2-dev \
    libffi \
    libffi-dev \
    libxslt-dev \
	build-base \
  && pip install scrapy \
  && rm -rf /var/cache/apk/*
  
ENV TZ Asia/Shanghai
