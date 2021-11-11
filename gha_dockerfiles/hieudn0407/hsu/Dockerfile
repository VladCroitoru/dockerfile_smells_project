FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
COPY . /app
WORKDIR /app
 
EXPOSE 5000/tcp
CMD ASPNETCORE_URLS=http://*:5000 dotnet ecom.hsu.vn.dll
ENV ASPNETCORE_ENVIRONMENT docker
