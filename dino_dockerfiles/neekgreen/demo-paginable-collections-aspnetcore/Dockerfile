FROM microsoft/aspnetcore-build:latest AS build-env
WORKDIR /app

# copy csproj and restore as distinct layers
COPY ./src/demo/demo.csproj ./
RUN dotnet restore

# copy and build everything else
COPY ./src/demo/ ./
RUN dotnet publish -c Release -o out

WORKDIR /app
COPY --from=build-env /app/out .

ENV ASPNETCORE_URLS http://+:80
EXPOSE 80 

ENTRYPOINT ["dotnet", "demo.dll"]