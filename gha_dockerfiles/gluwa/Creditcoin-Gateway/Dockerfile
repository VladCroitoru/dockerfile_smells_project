FROM mcr.microsoft.com/dotnet/sdk:3.1-focal AS build-env
WORKDIR /app

# Copy contents and restore as separate layers
COPY . .
# RUN dotnet restore CCGatewayPlugin/*.csproj
# RUN dotnet restore ccgateway/plugins/bitcoin/*.csproj
# RUN dotnet restore ccgateway/plugins/bitcoin/*.csproj
# RUN dotnet restore ccgateway/plugins/bitcoin/*.csproj
# RUN dotnet restore ccgateway/plugins/bitcoin/*.csproj
# RUN dotnet restore ccgateway/*.csproj
RUN dotnet restore

# Build projects
RUN dotnet publish ccgateway/plugins/bitcoin/*.csproj -c Release -o plugin-out
RUN dotnet publish ccgateway/plugins/erc20/*.csproj -c Release -o plugin-out
RUN dotnet publish ccgateway/plugins/ethereum/*.csproj -c Release -o plugin-out
RUN dotnet publish ccgateway/plugins/ethless/*.csproj -c Release -o plugin-out
RUN dotnet publish -c Release -o app-out

# Build runtime image
FROM mcr.microsoft.com/dotnet/sdk:3.1-focal
WORKDIR /home/Creditcoin/Gateway

COPY --from=build-env /app/app-out /home/Creditcoin/Gateway/
COPY --from=build-env /app/plugin-out /home/Creditcoin/Gateway/plugins/
