FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /source
COPY ./ContosoUniversity /source
RUN dotnet publish -r linux-musl-x64 --self-contained true -c Release -o /deploy

FROM mcr.microsoft.com/dotnet/runtime-deps:5.0-alpine-amd64 AS runtime

# Fix for gRPC in Alpine container
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.8/main' >> /etc/apk/repositories && \
    apk update --no-cache && \
    apk add --no-cache bash libc6-compat=1.1.19-r11

WORKDIR /app
COPY --from=build /deploy .

# Default port for Cloud Run
ENV ASPNETCORE_URLS="http://0.0.0.0:8080"

ENTRYPOINT ["/app/ContosoUniversity"]
