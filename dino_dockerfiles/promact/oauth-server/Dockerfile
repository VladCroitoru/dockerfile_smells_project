FROM promact/docker-dotnet-nodejs:latest
MAINTAINER Promact Infotech<info@promactinfo.com>

WORKDIR /app

COPY ./Promact.Oauth.Server/src/Promact.Oauth.Server/project.json .
COPY ./Promact.Oauth.Server/src/Promact.Oauth.Server/package.json .
COPY ./Promact.Oauth.Server/src/Promact.Oauth.Server/typings.json .
RUN npm install

COPY ./Promact.Oauth.Server/src/Promact.Oauth.Server/bower.json .
COPY ./Promact.Oauth.Server/src/Promact.Oauth.Server/.bowerrc .
RUN bower install --allow-root

# copy project.json and restore as distinct layers
COPY ./Promact.Oauth.Server/src/Promact.Oauth.Server ./

# copy and build everything else
RUN npm run build && gulp copytowwwroot && npm run bundle && mkdir /out
RUN dotnet restore
RUN dotnet publish project.json -c Release -o /out && cp appsettings.development.example.json /out/appsettings.production.json && rm -rf /app 
ENV ASPNETCORE_ENVIRONMENT Production
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["entrypoint.sh"]
