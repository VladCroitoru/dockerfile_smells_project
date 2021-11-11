FROM mcr.microsoft.com/dotnet/sdk:5.0-buster-slim as base

WORKDIR /app
ENV ASPNETCORE_URLS=http://+:80
EXPOSE 80

COPY . .
RUN dotnet build DockerTest.csproj --configuration=Debug -o /app/build

RUN dotnet dev-certs https --trust


ENTRYPOINT ["dotnet", "/app/build/DockerTest.dll"]

