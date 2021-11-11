# NETCORE BUILD
FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /app

# Install node@15.x
RUN curl -sL https://deb.nodesource.com/setup_15.x |  bash -
RUN apt-get install -y nodejs

COPY ./*.sln ./
COPY ./K9OCRS ./K9OCRS/

RUN dotnet restore
RUN dotnet publish -o /app/build

# RUNTIME
FROM mcr.microsoft.com/dotnet/aspnet:5.0

# Set Default Time Zone
RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=false
ENV DOTNET_SHUTDOWNTIMEOUTSECONDS=25

WORKDIR /app

COPY --from=build /app/build ./

RUN chmod +x ./K9OCRS

# ENTRYPOINT ["./IgniteVMS"]
CMD ASPNETCORE_URLS=http://*:$PORT ./K9OCRS