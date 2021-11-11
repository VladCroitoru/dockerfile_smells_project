# escape=`
FROM mcr.microsoft.com/windows/servercore:ltsc2019 as grok

RUN md c:\temp

RUN powershell -Command `
    Invoke-WebRequest -Method Get -Uri https://github.com/fstab/grok_exporter/releases/download/v1.0.0.RC5/grok_exporter-1.0.0.RC5.windows-amd64.zip -OutFile c:\grok_exporter.zip ; `
    Expand-Archive 'c:\grok_exporter.zip' -DestinationPath c:\temp


# Indicates that the windowsservercore image will be used as the base image.
FROM mcr.microsoft.com/windows/servercore:ltsc2019
LABEL maintainer="https://github.com/jmservera"                                         `
    org.opencontainers.image.authors="https://github.com/jmservera"                     `
    org.opencontainers.image.url="[pending]"                                            `
    org.opencontainers.image.title="VB6 PoC"                                             `
    org.opencontainers.image.description="Windows container with a small VB6 PoC"  `
    org.opencontainers.image.source="https://github.com/jmservera/legacyvb6ink8s" 

RUN md c:\app c:\temp c:\grok
WORKDIR c:\app

COPY .\app\MSWINSCK.OCX c:\app
RUN regsvr32 /s c:\app\MSWINSCK.OCX

# install prometheus exporter
RUN powershell -Command `
    Invoke-WebRequest -Method Get -Uri https://github.com/prometheus-community/windows_exporter/releases/download/v0.16.0/windows_exporter-0.16.0-amd64.msi -OutFile c:\windows_exporter.msi ; `
    start-Process msiexec -ArgumentList '/i c:\\windows_exporter.msi /passive /qn /log c:\\temp\\windows_exporter-install.txt ' -Wait ; `
    Remove-Item c:\windows_exporter.msi -Force ;

# install grok exporter
COPY --from=grok c:\temp\grok_exporter-1.0.0.RC5.windows-amd64 c:\grok

       # app port   # windows exporter  # grok exporter
EXPOSE 9001         9182                9144

COPY .\app c:\app

CMD ["start.bat"]