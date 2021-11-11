FROM mcr.microsoft.com/dotnet/sdk:5.0 as build
WORKDIR /build
RUN git clone --depth=1 -b separation https://github.com/Coflnet/HypixelSkyblock.git dev
RUN mkdir -p /build/skyblock/External/api
RUN git clone --depth=1 https://github.com/Ekwav/Hypixel.NET.git
WORKDIR /build/SkyCommand
COPY SkyUpdater.csproj .
RUN dotnet restore
COPY . .
RUN dotnet publish -c release

FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app

COPY --from=build /build/SkyCommand/bin/release/net5.0/publish/ .
RUN mkdir /data
ENV ASPNETCORE_URLS=http://+:8000;http://+:80

ENTRYPOINT ["dotnet", "SkyUpdater.dll", "--hostBuilder:reloadConfigOnChange=false"]

VOLUME /data

