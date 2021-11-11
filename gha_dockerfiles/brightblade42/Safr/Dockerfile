#FROM mcr.microsoft.com/dotnet/aspnet:5.0
#FROM mcr.microsoft.com/dotnet/sdk:5.0
FROM mcr.microsoft.com/dotnet/sdk:5.0.102-ca-patch-buster-slim
#external | internal
ENV IMG_URL_TYPE="external"
#not used yet
ENV ENROLL_CONF="1.00"
#not used yet
ENV IDENT_CONF="0.92"
WORKDIR /app
COPY .publish /app
COPY extra/build_data /app/data
RUN apt update && apt install -y sqlite3 vim
EXPOSE 8085
EXPOSE 443
ENTRYPOINT ["dotnet", "Safr.Server.dll"]
