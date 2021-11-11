FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build-env
WORKDIR /app

COPY ./src/KinoDnesApi/*.csproj ./KinoDnesApi/
RUN dotnet restore KinoDnesApi

COPY ./src/ ./
RUN dotnet publish KinoDnesApi -c Release -o ./../out

FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=build-env /out .

USER 5000
CMD ASPNETCORE_URLS=http://*:$PORT dotnet KinoDnesApi.dll
