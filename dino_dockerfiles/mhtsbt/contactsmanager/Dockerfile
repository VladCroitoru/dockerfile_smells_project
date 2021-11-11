FROM microsoft/dotnet:1.1.2-sdk

ENV ASPNETCORE_ENVIRONMENT Production

COPY ContactsManager /app
WORKDIR /app


EXPOSE 5000

RUN dotnet restore


ENTRYPOINT ["dotnet","run"]