### STAGE 1: Build ###

# We label our stage as 'builder'
FROM microsoft/dotnet:2.2-sdk as builder

# Change the workdir to the source dir
WORKDIR /src

# Copy the code to the docker image
COPY /src .

## Build the app and publish in app folder
RUN dotnet publish --output /app/ --configuration Release

### STAGE 2: Setup ###
# This is the runtime image
FROM microsoft/dotnet:2.2-aspnetcore-runtime

WORKDIR /app
 
# Copy some required files
 
# Copy build output file to use swagger
COPY --from=builder /src/main/bin/Debug/netcoreapp2.2/seed_dotnet.xml .
 
 
# Copy database  
COPY  --from=builder /src/main/*.db .
 
# Copy build output 
COPY --from=builder /app .
 
ENTRYPOINT ["dotnet", "main.dll --launch-profile seed-dotnet]
