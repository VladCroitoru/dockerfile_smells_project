# NOTE: Microsoft no longer provides the windows mssql docker image
# https://cloudblogs.microsoft.com/sqlserver/2019/07/01/sql-server-2019-on-windows-containers-now-in-early-adopters-program/
# https://web.archive.org/web/20210524143153/https://docs.microsoft.com/en-us/windows-server/get-started-19/servicing-channels-19
# https://freddysblog.com/2020/10/12/troubleshooting-business-central-on-docker/
# https://freddysblog.com/2018/12/11/clean-up-after-yourself-docker-your-mom-isnt-here/

FROM mssql-server-windows-developer:2017-alt

LABEL Name=mssql-ssrs-windows-developer Version=2017-1.0 maintainer="Ralph O"

# ENV exe "https://download.microsoft.com/download/E/6/4/E6477A2A-9B58-40F7-8AD6-62BB8491EA78/SQLServerReportingServices.exe"

COPY SQLServerReportingServices.exe /
ENV exe "SQLServerReportingServices.exe"

ENV sa_password="_" \
    attach_dbs="[]" \
    ACCEPT_EULA="_" \
    sa_password_path="C:\ProgramData\Docker\secrets\sa-password" \
    ssrs_user="_" \
    ssrs_password="_" \
    SSRS_edition="DEV" \
    ssrs_password_path="C:\ProgramData\Docker\secrets\ssrs-password"

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

# make install files accessible
COPY start.ps1 /
COPY configureSSRS2017.ps1 /
COPY sqlstart.ps1 /
COPY newadmin.ps1 /

WORKDIR /

# RUN  Invoke-WebRequest -Uri $env:exe -OutFile SQLServerReportingServices.exe ; \
#     Start-Process -Wait -FilePath .\SQLServerReportingServices.exe -ArgumentList "/quiet", "/norestart", "/IAcceptLicenseTerms", "/Edition=$env:SSRS_edition" -PassThru -Verbose

RUN Start-Process -Wait -FilePath .\SQLServerReportingServices.exe -ArgumentList "/quiet", "/norestart", "/IAcceptLicenseTerms", "/Edition=$env:SSRS_edition" -PassThru -Verbose

CMD .\start -sa_password $env:sa_password -ACCEPT_EULA $env:ACCEPT_EULA -attach_dbs \"$env:attach_dbs\" -ssrs_user $env:ssrs_user -ssrs_password $env:ssrs_password -Verbose

