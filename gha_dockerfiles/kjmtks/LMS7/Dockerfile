FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster
WORKDIR /app
EXPOSE 80

RUN apt-get update -y && apt-get upgrade -yq && apt-get install -y curl git gnupg &&\
    curl -sL https://deb.nodesource.com/setup_10.x | bash - &&\
    apt-get install -y nodejs &&\
    apt-get install -yq binutils debootstrap &&\
    dotnet tool install --global dotnet-ef && export PATH="$PATH:/root/.dotnet/tools"

COPY *.sln .
COPY ALMS.App/*.csproj ./ALMS.App/
RUN mkdir -p /data/users && rm -rf ./AMLS.App/wwwroot/css/themes

COPY ALMS.App/. ./ALMS.App/
WORKDIR /app/ALMS.App
RUN npm install
RUN dotnet restore
RUN dotnet publish -c Release -o out

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
