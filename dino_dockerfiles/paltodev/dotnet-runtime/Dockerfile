FROM microsoft/dotnet:2.1.3-aspnetcore-runtime

RUN apt-get update
RUN apt-get install -y \
    mysql-client \
    ca-certificates \
    curl \
    software-properties-common \
    python \
    python-pip \
    redis-tools \
    git

RUN apt install tzdata
