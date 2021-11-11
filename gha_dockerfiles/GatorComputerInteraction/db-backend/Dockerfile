FROM mcr.microsoft.com/dotnet/sdk:3.1-alpine as builder

WORKDIR /build
ADD WebAPI/ .
RUN dotnet restore
RUN dotnet publish -c release -o /app --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:3.1-alpine

WORKDIR /app
COPY --from=builder /app .

CMD ["dotnet", "WebAPI.dll", "--urls", "http://0.0.0.0:8080"]
