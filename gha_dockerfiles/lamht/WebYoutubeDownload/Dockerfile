#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster AS build
WORKDIR /src
COPY ["WebYoutubeDownload/WebYoutubeDownload.csproj", "WebYoutubeDownload/"]
RUN dotnet restore "WebYoutubeDownload/WebYoutubeDownload.csproj"
COPY . .
WORKDIR "/src/WebYoutubeDownload"
RUN dotnet build "WebYoutubeDownload.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "WebYoutubeDownload.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
RUN apt update && apt install wget -y && apt install python3.7 -y && apt install ffmpeg -y \
   && wget https://yt-dl.org/latest/youtube-dl -O /usr/local/bin/youtube-dl && chmod a+x /usr/local/bin/youtube-dl \
   && ln -s /usr/bin/python3.7 /usr/local/bin/python
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WebYoutubeDownload.dll"]