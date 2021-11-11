FROM mcr.microsoft.com/dotnet/aspnet:5.0
WORKDIR /app1
COPY ./bin/Release/net5.0/publish .
ENTRYPOINT ["dotnet", "myWebApp.dll"]
EXPOSE 8080
ENV ASPNETCORE_URLS=http://*:8080

