# https://hub.docker.com/_/microsoft-dotnet
FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /source

# copy csproj and restore as distinct layers
COPY src/Api/*.csproj Api/
COPY src/Core/*.csproj Core/
RUN dotnet restore Api/Api.csproj

# copy and build app and libraries
COPY src/Api/ Api/
COPY src/Core/ Core/
WORKDIR /source/Api
RUN dotnet build -c release

FROM build AS publish
RUN dotnet publish -c release --no-build -o /app

# final stage/image
FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app
COPY --from=publish /app .

#CMD ["dotnet", "Api.dll"]

CMD ASPNETCORE_URLS=http://*:$PORT dotnet Api.dll