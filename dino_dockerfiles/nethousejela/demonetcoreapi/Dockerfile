FROM microsoft/dotnet:latest
ENTRYPOINT ["dotnet", "DemoNetCoreApi.dll"]
ARG source=.
WORKDIR /app
EXPOSE 80
COPY $source .
