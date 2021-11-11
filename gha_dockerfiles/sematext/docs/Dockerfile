FROM python:2.7-alpine

ENV BOOTSWATCH_VERSION 0.4.0
RUN apk --no-cache add tar curl lftp ca-certificates openssh && \
    pip install mkdocs===0.17.3 && \
    pip install mkdocs-material===2.7.0 && \
    pip install Markdown && \
    pip install markdown-fenced-code-tabs
RUN mkdir /workspace
WORKDIR /workspace
RUN curl -o mkdocs-bootswatch.tar.gz -SL "https://github.com/mkdocs/mkdocs-bootswatch/archive/$BOOTSWATCH_VERSION.tar.gz" && \
    tar -xzf mkdocs-bootswatch.tar.gz --strip-components=1 -C . && \
    rm mkdocs-bootswatch.tar.gz
COPY . .
RUN mkdocs build