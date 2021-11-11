FROM mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:5.0-buster-slim AS build

# Install NodeJs
RUN apt-get update && \
apt-get install -y wget && \
apt-get install -y gnupg2 && \
wget -qO- https://deb.nodesource.com/setup_16.x | bash - && \
apt-get install -y build-essential nodejs
# End Install

WORKDIR /src

COPY ["src/DocumentSink/DocumentSink.csproj", "DocumentSink/"]
COPY ["src/DocumentSink.Core/DocumentSink.Core.csproj", "DocumentSink.Core/"]
COPY ["src/DocumentSink.ClientLib/DocumentSink.ClientLib.csproj", "DocumentSink.ClientLib/"]

RUN dotnet restore "DocumentSink/DocumentSink.csproj"

COPY "src/DocumentSink/" "DocumentSink/"
COPY "src/DocumentSink.Core/" "DocumentSink.Core/"
COPY "src/DocumentSink.ClientLib/" "DocumentSink.ClientLib/"

WORKDIR "/src/DocumentSink"

RUN dotnet build "DocumentSink.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "DocumentSink.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "DocumentSink.dll"]