FROM mcr.microsoft.com/powershell:alpine-3.10
RUN apk add --no-cache mysql-client
RUN mkdir /powershell
RUN touch /powershell/.config
WORKDIR /powershell
COPY webmon.ps1 /powershell
COPY webquery.ps1 /powershell
COPY add.ps1 /powershell
COPY delete.ps1 /powershell
CMD pwsh webmon.ps1