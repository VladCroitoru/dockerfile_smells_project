FROM microsoft/iis
COPY ./build-Index.ps1 /
ENV useCustomPath=false pageText=Home
SHELL ["powershell", "-Command"]
ENTRYPOINT .\build-Index.ps1;C:\ServiceMonitor.exe w3svc 
