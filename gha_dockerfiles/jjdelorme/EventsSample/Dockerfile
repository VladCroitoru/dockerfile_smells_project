# Build the API
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS api-build
WORKDIR /src
COPY /api .
RUN dotnet publish -r linux-x64 --self-contained true -p:PublishSingleFile=true -c Release -o /publish

# Build the static web site
FROM node:lts AS web-build
WORKDIR /src
COPY /web .
RUN npm install -g react-scripts && npm install
RUN BUILD_PATH='/wwwroot' \
    REACT_APP_VERSION=$(npm -s run env echo '$npm_package_version') \
    react-scripts build

# Combine both into the final container
FROM mcr.microsoft.com/dotnet/runtime-deps:6.0 as runtime
WORKDIR /app
COPY --from=api-build /publish .
COPY --from=web-build /wwwroot ./wwwroot/

# Use the default port for Cloud Run
ENV ASPNETCORE_URLS=http://0.0.0.0:8080

ENTRYPOINT ["./EventsSample"]