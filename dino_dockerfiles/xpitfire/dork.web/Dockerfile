FROM microsoft/dotnet:1.0.0-preview2-onbuild

COPY src /dotnetapp
WORKDIR /dotnetapp/Dork.Web

RUN dotnet restore
RUN dotnet build

EXPOSE 5000/tcp
ENV ASPNETCORE_URLS http://*:5000

ENTRYPOINT ["dotnet", "run"]