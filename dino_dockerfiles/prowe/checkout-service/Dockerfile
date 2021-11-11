FROM microsoft/aspnetcore-build AS builder

WORKDIR /source

# caches restore result by copying csproj file separately
COPY *.csproj .
RUN dotnet restore

# copies the rest of your code
COPY . .
RUN dotnet publish --output /app/ --configuration Release
RUN dotnet ef database update \
    && mv data.db /app/

# Stage 2
FROM microsoft/aspnetcore

EXPOSE 5000
ENV ASPNETCORE_URLS "http://0.0.0.0:5000"

WORKDIR /app
COPY --from=builder /app .



ENTRYPOINT ["dotnet", "checkout-service.dll"]