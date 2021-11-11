FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine AS sdk
WORKDIR /app
COPY . .
RUN dotnet restore --runtime alpine-x64
RUN dotnet publish ./Tenderhack.Api/Tenderhack.Api.csproj --runtime alpine-x64 --configuration Release --no-restore --output ./publish
FROM mcr.microsoft.com/dotnet/runtime-deps:6.0-alpine as runtime
WORKDIR /app
COPY --from=sdk /app/publish .
ENTRYPOINT ["./Tenderhack.Api"]
CMD ["--serve"]
