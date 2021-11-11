FROM ubuntu:xenial

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        apt-transport-https \
&& rm -rf /var/lib/apt/lists/*

RUN sh -c 'echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list'

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893 \
    && apt-get update \
    && apt-get install -y dotnet-dev-1.0.1

RUN mkdir /usr/share/app
COPY . /usr/share/app

WORKDIR /usr/share/app/src/devWarsztaty-ScoringService

RUN dotnet restore \
    && dotnet build

EXPOSE 5001

CMD ["dotnet", "run"]