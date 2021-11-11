FROM microsoft/dotnet:1.1.1-sdk

EXPOSE 5000
EXPOSE 40000
EXPOSE 40001

ADD . /app

RUN cd /app/Silo \
    && dotnet restore \
    && dotnet build

RUN cd /app/FrontEnd \
    && dotnet restore \
    && dotnet build

WORKDIR /app
