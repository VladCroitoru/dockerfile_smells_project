# Stage 1
FROM microsoft/aspnetcore-build:2.0 AS builder
WORKDIR /source

COPY . .
RUN dotnet restore Matterhook.NET/Matterhook.NET.csproj
RUN dotnet publish Matterhook.NET/Matterhook.NET.csproj -c Release -o /publish

# Stage 2
FROM microsoft/aspnetcore:2.0
WORKDIR /app
EXPOSE 80
COPY --from=builder /publish .
ENTRYPOINT ["dotnet", "Matterhook.NET.dll"]
