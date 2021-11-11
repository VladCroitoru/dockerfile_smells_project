
## DOTNET BUILD
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS BUILD
WORKDIR /app

# copy everything
COPY . .

# dotnet commands use the solution file in root for building things.
# If you get weird errors due check that .sln file is committed to repo!
RUN dotnet restore
RUN dotnet publish -c Release -o out
RUN dotnet test --no-restore

## DOTNET RUNTIME
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS RUNTIME
WORKDIR /app

COPY --from=BUILD /app/out ./
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

# Make sure the app binds to port 8080 
ENV ASPNETCORE_URLS http://*:8080

ENTRYPOINT ["./docker-entrypoint.sh"]
