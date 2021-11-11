FROM microsoft/windowsservercore:latest
MAINTAINER @csciborg
ENV NginxVersion 1.13.1
ENV WriteReverseProxyConfFromEnv=true \
    ReverseProxyListenPort=80 \
    ReverseProxyServerName=nginx \
	ReverseProxyLocationList=@() \
    EnabledSitesPath=c:\\nginx\\enabled-sites \
    EnableNginxWebServer=true \
	NginxConfFile=c:\\nginx\\nginx-${NginxVersion}\\conf\\nginx.conf
EXPOSE ${ReverseProxyListenPort}

SHELL ["powershell", "-command"]
RUN Invoke-WebRequest "http://nginx.org/download/nginx-$($env:NginxVersion).zip" -OutFile C:\nginx.zip; \
    Expand-Archive C:\nginx.zip C:\nginx ; \
    Remove-Item "C:\nginx\nginx-$($env:NginxVersion)\conf\*.conf" -Verbose; \
	New-Item -type directory "$($env:EnabledSitesPath)"; \
	Remove-Item C:\nginx.zip;

WORKDIR /nginx/nginx-${NginxVersion}
COPY ./conf/* ./conf/

ENTRYPOINT .\conf\Generate-ReverseProxyConf.ps1;.\nginx.exe -c $env:NginxConfFile