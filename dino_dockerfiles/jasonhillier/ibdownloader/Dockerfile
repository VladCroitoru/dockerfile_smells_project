FROM microsoft/dotnet:2.1-sdk

RUN apt-get update && apt-get install -y net-tools telnet tmux nano

ADD . /ibdownloader
WORKDIR ibdownloader
RUN dotnet build -c release

WORKDIR /ibdownloader/IBDownloader/bin/Release/netcoreapp2.0

ENV IB_HOST=locahost
ENV IB_PORT=7982

ENTRYPOINT ["dotnet", "IBDownloader.dll"]
