FROM mcr.microsoft.com/dotnet/sdk:5.0-alpine

WORKDIR /app

#copy the code in
COPY ./TbspRpgApi /app
COPY ./TbspRpgDataLayer /TbspRpgDataLayer
COPY ./TbspRpgSettings /TbspRpgSettings
COPY ./TbspRpgProcessor /TbspRpgProcessor

#build the site
RUN dotnet restore

#run the site
#RUN dotnet watch run --project ./app.csproj
ENTRYPOINT ["dotnet", "watch", "run", "--urls", "http://0.0.0.0:8000"]
