FROM mcr.microsoft.com/dotnet/sdk:5.0-alpine as build
WORKDIR /app
COPY . .
RUN dotnet publish -c Release

FROM mcr.microsoft.com/dotnet/aspnet:5.0-alpine
WORKDIR /app
COPY --from=build /app/bin/Release/net5.0/publish/ .
CMD [ "dotnet", "graphium-api.dll" ]
