FROM mcr.microsoft.com/dotnet/core/sdk:2.2

WORKDIR /app
ADD ./Shared ./Silo ./*.sln ./

RUN dotnet build

CMD dotnet run --no-build
