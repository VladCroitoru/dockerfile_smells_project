FROM microsoft/aspnetcore-build:2.0
WORKDIR /app

# copy csproj and restore packages
COPY *.csproj ./
RUN dotnet restore

# copy and build everything else
COPY . ./
RUN dotnet publish -c Release -o out

# Listen on port 80
EXPOSE 80
ENV ASPNETCORE_URLS=http://+:80

ENTRYPOINT ["dotnet", "out/FirstDockerApp.dll"]
