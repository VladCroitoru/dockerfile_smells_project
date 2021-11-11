# Build image
FROM microsoft/dotnet:2.0.3-sdk AS builder
WORKDIR /sln
COPY ./LF-Tenant.sln ./NuGet.config  ./

# Copy all the csproj files and restore to cache the layer for faster builds
# cache the intermediate images so _much_ faster
COPY ./src/LF-Tenant.Abstractions/LF-Tenant.Abstractions.csproj  ./src/LF-Tenant.Abstractions/LF-Tenant.Abstractions.csproj
COPY ./src/LF-Tenant.Data/LF-Tenant.Data.csproj  ./src/LF-Tenant.Data/LF-Tenant.Data.csproj
COPY ./src/LF-Tenant.Business/LF-Tenant.Business.csproj  ./src/LF-Tenant.Business/LF-Tenant.Business.csproj
COPY ./src/LF-Tenant.Api/LF-Tenant.Api.csproj  ./src/LF-Tenant.Api/LF-Tenant.Api.csproj
RUN dotnet clean
RUN dotnet restore


COPY ./src ./src

RUN dotnet build -c Release --no-restore


RUN dotnet publish "./src/LF-Tenant.Api/LF-Tenant.Api.csproj" -c Release -o "../../dist" --no-restore

#App image
FROM microsoft/aspnetcore:2.0.3
WORKDIR /app
ENV ASPNETCORE_ENVIRONMENT Development
ENTRYPOINT ["dotnet", "LF-Tenant.Api.dll"]
COPY --from=builder /sln/dist .