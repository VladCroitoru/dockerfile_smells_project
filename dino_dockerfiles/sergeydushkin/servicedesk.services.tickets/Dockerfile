FROM microsoft/dotnet:1.1.1-sdk
COPY ./servicedesk.Services.Tickets /app
WORKDIR /app
 
RUN ["dotnet", "restore", "--source", "https://api.nuget.org/v3/index.json", "--source", "https://www.myget.org/F/sergeydushkin/api/v3/index.json", "--no-cache"]
RUN ["dotnet", "build"]
 
EXPOSE 10020/tcp
ENV ASPNETCORE_URLS http://*:10020
ENV ASPNETCORE_ENVIRONMENT docker
 
ENTRYPOINT ["dotnet", "run"]