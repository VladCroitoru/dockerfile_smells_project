# stage 1
FROM mcr.microsoft.com/dotnet/sdk:5.0-buster-slim as builder

# suppress data collection
ENV DOTNET_CLI_TELEMETRY_OPTOUT 1

# caches restore result by copying csproj file separately
WORKDIR /source/faas-run/
COPY src/faas-run.csproj .

# restore packages
RUN dotnet restore

# Copies the rest of the code
COPY src/. .

# build and publish
RUN dotnet publish -c release -r linux-x64 --no-self-contained /p:PublishSingleFile=true -o published faas-run.csproj

# stage 2
FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /home/app/
COPY --from=builder /source/faas-run/published/faas-run /usr/bin/
