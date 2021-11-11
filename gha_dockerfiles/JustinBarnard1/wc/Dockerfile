FROM mcr.microsoft.com/dotnet/core/sdk:3.1
COPY bin/Release/netcoreapp3.1/publish/ App/
WORKDIR /App
CMD ASPNETCORE_URLS=http://*:$PORT dotnet Keepr.dll