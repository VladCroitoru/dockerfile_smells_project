# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/dotnet/aspnet:3.1
COPY bin/Release/netcoreapp3.1/publish/ App/
COPY ./Engine/resources/stopwords.txt App/Engine/resources/stopwords.txt
WORKDIR /App
EXPOSE 80
ENTRYPOINT ["dotnet", "Axle.dll"]
