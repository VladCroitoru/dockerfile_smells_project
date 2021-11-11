FROM microsoft/dotnet:1.0.0-preview2-sdk
MAINTAINER Giovanni Bassi <giggio@giggio.net>

RUN mkdir /repo & \
    mkdir /app
VOLUME /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y git curl build-essential vim
RUN git clone https://github.com/Lambda3/dotnet-commands.git /repo && \
    cd /repo && \
    git remote add ssh git@github.com:Lambda3/dotnet-commands.git

# run with `docker run -ti --name dotnet-commands -v "$(pwd):/app" lambda3/dotnet-commands`