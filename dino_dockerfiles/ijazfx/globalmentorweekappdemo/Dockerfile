FROM microsoft/dotnet:1.0.0-preview2-sdk

ENV ASPNETCORE_URLS http://*:5000

COPY . /app

WORKDIR /app
 
RUN ["dotnet", "restore"]
 
RUN ["dotnet", "build"]
 
EXPOSE 5000
 
ENTRYPOINT ["dotnet", "run"]