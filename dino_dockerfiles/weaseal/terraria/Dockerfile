FROM alpine:3.3

MAINTAINER Walt Venable <weaseal@gmail.com>

# This step will not be necessary once mono is out of testing
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk update && apk upgrade && apk add mono

# fix for favorites.json error
RUN favorites_path="/root/My Games/Terraria" && mkdir -p "$favorites_path" && echo "{}" > "$favorites_path/favorites.json"

# Download and install TShock
ENV TSHOCK_VERSION 4.3.12
ENV TSHOCK_FILE_POSTFIX ""

ADD https://github.com/NyxStudios/TShock/releases/download/v${TSHOCK_VERSION}/tshock_${TSHOCK_VERSION}.zip /
RUN mkdir /tshock
RUN unzip tshock_${TSHOCK_VERSION}.zip -d /tshock
RUN rm tshock_${TSHOCK_VERSION}.zip

# Allow for external data
VOLUME ["/world", "/tshock/ServerPlugins"]

# Set working directory to server
WORKDIR /tshock

# Set permissions
RUN chmod 777 TerrariaServer.exe

# run the server
ENTRYPOINT ["mono", "--server", "--gc=sgen", "-O=all", "TerrariaServer.exe", "-configpath", "/world", "-worldpath", "/world", "-logpath", "/world"]
