FROM microsoft/dotnet:2.0.5-sdk-2.1.4

RUN apt-get update
RUN apt-get install -y \
    mono-complete \
    libgit2-dev unzip libssl1.0 libcurl3 jq

WORKDIR /build

COPY build.sh .
COPY preload.cake .
COPY setup.sh .

RUN chmod +x build.sh
RUN chmod +x setup.sh

RUN ./build.sh -s preload.cake
RUN ./setup.sh

WORKDIR /usr/bin
RUN ln -s /build/build.sh cake

RUN curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
