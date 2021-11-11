FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /ordermanager-dotnet
COPY . .
RUN dotnet restore
RUN dotnet build --no-restore -c Release -o /app

FROM build AS publish
RUN dotnet publish --no-restore -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
# ASP.NET container pattern
# ENTRYPOINT ["dotnet", "CarterAPI.dll"]
# Option used by Heroku
# Created by Leandro Cunha
# Documentation: https://hub.docker.com/_/microsoft-dotnet-sdk/
CMD ASPNETCORE_URLS=http://*:$PORT dotnet ordermanager-dotnet.dll
