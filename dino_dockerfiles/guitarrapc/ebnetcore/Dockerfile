FROM microsoft/aspnetcore-build:2.0 as build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY src/*.csproj ./
RUN dotnet restore

# copy and build everything else
COPY src/. ./
RUN dotnet publish -c Release -o out

# build runtime image
FROM microsoft/aspnetcore:2.0
WORKDIR /app
COPY --from=build /app/out .
EXPOSE 80
ENTRYPOINT ["dotnet", "ebnetcore.dll"]