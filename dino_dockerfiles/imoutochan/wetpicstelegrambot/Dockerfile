FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:5.0-alpine AS build
WORKDIR /src
COPY *.sln ./
COPY NuGet.config ./
COPY WetPicsTelegramBot.WebApp/WetPicsTelegramBot.WebApp.csproj WetPicsTelegramBot.WebApp/
COPY WetPicsTelegramBot.Data/WetPicsTelegramBot.Data.csproj WetPicsTelegramBot.Data/
COPY PixivApi/PixivApi.csproj PixivApi/
RUN dotnet restore "WetPicsTelegramBot.WebApp/WetPicsTelegramBot.WebApp.csproj"
COPY . .
WORKDIR /src/WetPicsTelegramBot.WebApp
RUN dotnet build -c Release -o /app

FROM build AS publish
RUN dotnet publish -c Release -o /app

FROM base AS final
WORKDIR /app
RUN apt-get update
RUN apt-get install -y libgdiplus
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "WetPicsTelegramBot.WebApp.dll"]
