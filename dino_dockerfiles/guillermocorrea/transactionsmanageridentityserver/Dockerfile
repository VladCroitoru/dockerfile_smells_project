FROM microsoft/aspnetcore-build AS build

WORKDIR /code

COPY . .

RUN dotnet restore

RUN dotnet publish --output /output --configuration Release

FROM microsoft/aspnetcore

COPY --from=build /output /app

WORKDIR /app

ENTRYPOINT [ "dotnet", "TransactionsManagerIdentityServer.dll" ]