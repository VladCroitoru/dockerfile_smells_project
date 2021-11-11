FROM mcr.microsoft.com/dotnet/sdk:3.1 AS builder

WORKDIR /source
COPY ./src .
RUN dotnet restore
RUN dotnet publish ./Api.Application --output /app/

FROM mcr.microsoft.com/dotnet/aspnet:3.1
WORKDIR /app
COPY --from=builder /app .
EXPOSE 5000
ENTRYPOINT ["dotnet", "application.dll"]