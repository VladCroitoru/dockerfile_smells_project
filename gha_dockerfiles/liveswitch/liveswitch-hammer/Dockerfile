FROM mcr.microsoft.com/dotnet/sdk:3.1 AS build
WORKDIR /app

COPY FM.LiveSwitch.Hammer.sln FM.LiveSwitch.Hammer.sln
COPY src src
COPY .git .git
RUN dotnet restore
RUN dotnet publish src/FM.LiveSwitch.Hammer/FM.LiveSwitch.Hammer.csproj -c Release -o lib
RUN rm -rf src
RUN rm -rf .git
RUN rm FM.LiveSwitch.Hammer.sln

FROM mcr.microsoft.com/dotnet/runtime:3.1
WORKDIR /app
COPY --from=build /app/lib .

ENTRYPOINT ["dotnet", "lshammer.dll"]