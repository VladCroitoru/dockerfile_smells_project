## Build stage
FROM microsoft/aspnetcore-build AS builder

# Set the working directory to the app directory
WORKDIR /source

# caches restore result by copying csproj file separately
COPY *.csproj .
RUN dotnet restore

# copies the rest of your code
COPY . .
RUN dotnet publish --output /app/ --configuration Release

# build runtime image
FROM microsoft/aspnetcore
WORKDIR /app
COPY --from=builder /app .
EXPOSE 8080

# Define environment variables
# Application Insights
ENV APPINSIGHTS_KEY=
ENV CHALLENGEAPPINSIGHTS_KEY=23c6b1ec-ca92-4083-86b6-eba851af9032

# Challenge Logging
ENV TEAMNAME=

# AMQP
ENV AMQPURL=

# Mongo/Cosmos
ENV MONGOURL=


ENTRYPOINT ["dotnet", "captureorderack.dll"]
