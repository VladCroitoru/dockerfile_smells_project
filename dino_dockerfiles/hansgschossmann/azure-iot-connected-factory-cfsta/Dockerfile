ARG base_tag=3.1-alpine

# copy and publish app
FROM mcr.microsoft.com/dotnet/core/sdk:${base_tag} AS build
WORKDIR /build
COPY . .
RUN dotnet publish -c Release -o /build/out

# start app
FROM mcr.microsoft.com/dotnet/core/runtime:${base_tag} AS runtime
RUN apk add --no-cache tzdata
WORKDIR /app
COPY --from=build /build/out .
WORKDIR /appdata
ENTRYPOINT ["dotnet", "/app/CfStation.dll"]