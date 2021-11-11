# syntax = docker/dockerfile:1.0-experimental

FROM blackpoker/blackpoker-doc-base:latest

# ------------------------------
# pip
# ------------------------------
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# ------------------------------
# source
# ------------------------------
WORKDIR /
RUN mkdir source && \
 chown 1000:1000 source && \
 chmod 777 source

COPY ./source/* source/.

# ------------------------------
# 実行設定
# ------------------------------
RUN apk add --no-cache make
COPY ./docker-build.sh .

# ------------------------------
# 出力設定
# ------------------------------
VOLUME /docs

USER 1000:1000

# sphinx-build -b html ./source ./docs

# RUN echo "#!/bin/bash\nsphinx-build -b html ./source ./docs" > /build.sh


CMD ["sh","docker-build.sh"]

# docker build --pull --rm -f "Dockerfile" -t blackpoker-doc:latest "."
# docker run --rm -it -v `pwd`/docs:/docs blackpoker-doc:latest
