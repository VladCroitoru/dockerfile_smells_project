FROM microsoft/aspnetcore-build:2.0 AS build-env
LABEL maintainer="ademcatamak@gmail.com"

COPY . /ProjectRenamer
WORKDIR /ProjectRenamer
RUN dotnet restore

RUN dotnet publish -c Release -o out

# build runtime image
FROM microsoft/aspnetcore:2.0-jessie
WORKDIR /app
COPY --from=build-env /ProjectRenamer/ProjectRenamer.Api/out .

EXPOSE 80
HEALTHCHECK --interval=5s --timeout=3s --retries=3 CMD curl -f / http://localhost:80/health-check || exit 1 
ENTRYPOINT ["dotnet", "ProjectRenamer.Api.dll"]
