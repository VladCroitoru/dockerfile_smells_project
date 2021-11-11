FROM microsoft/dotnet:2.0-sdk
COPY src /build
WORKDIR /build/BikeShareSystem.Core
RUN dotnet restore
RUN dotnet publish -f netcoreapp2.0 -r ubuntu.16.10-x64 --self-contained

FROM ubuntu:16.10
RUN apt-get -y update
RUN apt-get -y install libunwind8 libunwind8-dev gettext libicu-dev liblttng-ust-dev libcurl4-openssl-dev libssl-dev uuid-dev unzip
COPY --from=0 /build/BikeShareSystem.Core/bin/Debug/netcoreapp2.0/ubuntu.16.10-x64/publish /app
WORKDIR /app
ENTRYPOINT ./BikeShareSystem.Core /data/settings.json