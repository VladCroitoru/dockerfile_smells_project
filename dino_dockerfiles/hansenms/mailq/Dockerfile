FROM microsoft/dotnet:2.0.5-sdk-2.1.4-jessie
WORKDIR /app

COPY . ./

WORKDIR /app/MailQ
RUN dotnet restore
RUN dotnet publish -c Release -o out
ENTRYPOINT ["dotnet", "out/MailQ.dll"]


