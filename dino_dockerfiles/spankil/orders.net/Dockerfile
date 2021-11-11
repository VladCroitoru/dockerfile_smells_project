FROM microsoft/dotnet:latest

RUN ls -ltr

COPY . /app
WORKDIR /app

RUN ls -ltr

RUN ["dotnet", "restore"]
RUN apt-get update && apt-get install -y tcpdump jq

EXPOSE 80/tcp

ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:80"]
