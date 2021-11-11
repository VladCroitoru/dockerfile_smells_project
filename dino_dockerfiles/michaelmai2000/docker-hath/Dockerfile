FROM anapsix/alpine-java:7
MAINTAINER Luis Alvarado <alvaradorocks@gmail.com>

# Install dependencies 
RUN apk --no-cache add curl sqlite unzip

# Common
ENV HatH_VERSION 1.4.1
ENV HatH_DOWNLOAD_URL https://repo.e-hentai.org/hath/HentaiAtHome_$HatH_VERSION.zip
ENV HatH_DOWNLOAD_SHA256 811f31bd8472ca1f63b7e1cbb47c8f10185a613c1373004882af30fb8597d656
ENV HatH_USER hath
ENV HatH_PATH "/home/$HatH_USER/client"
ENV HatH_ARCHIVE hath.zip
ENV HatH_PORT 11112
ENV HatH_JAR HentaiAtHome.jar
ENV HatH_ARGS --use_more_memory --disable_logging --port "$HatH_PORT"

# Container Setup
RUN adduser -D "$HatH_USER" && \
    mkdir "$HatH_PATH" && \
    cd "$HatH_PATH" && \
    curl -fsSL "$HatH_DOWNLOAD_URL" -o "$HatH_ARCHIVE" && \
    echo -n ""$HatH_DOWNLOAD_SHA256"  "$HatH_ARCHIVE"" | sha256sum -c && \
    unzip "$HatH_ARCHIVE" && \
    rm "$HatH_ARCHIVE"

RUN mkdir -p "$HatH_PATH/cache" "$HatH_PATH/data" "$HatH_PATH/downloaded" "$HatH_PATH/hathdl" "$HatH_PATH/tmp"

COPY client/ "$HatH_PATH/"

RUN chmod -R 775 "$HatH_PATH"
WORKDIR "$HatH_PATH"

# Expose the port
EXPOSE "$HatH_PORT"

VOLUME ["$HatH_PATH/cache", "$HatH_PATH/data", "$HatH_PATH/downloaded", "$HatH_PATH/hathdl"]

CMD java -jar "$HatH_JAR"
