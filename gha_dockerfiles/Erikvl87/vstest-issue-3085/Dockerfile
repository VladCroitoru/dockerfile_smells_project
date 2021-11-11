FROM mcr.microsoft.com/dotnet/sdk:3.1.413-alpine3.14 AS build

# Required for System.Drawing;
RUN apk add libgdiplus --repository http://nl.alpinelinux.org/alpine/edge/testing --allow-untrusted

# Required for fonts.
RUN apk --no-cache add msttcorefonts-installer fontconfig && \
    update-ms-fonts && \
    fc-cache -f

WORKDIR /app

COPY . ./

RUN dotnet restore

RUN dotnet build \
    --configuration Release \
    --no-restore

ENTRYPOINT ["/bin/sh", "start.sh"]