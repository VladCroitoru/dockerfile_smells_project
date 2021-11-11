FROM node:12.16.2 as node-env
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY eform-angular-frontend/eform-client ./
RUN npm install
RUN npm run build

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build-env
WORKDIR /app
ARG GITVERSION
ARG PLUGINVERSION

# Copy csproj and restore as distinct layers
COPY eform-angular-frontend/eFormAPI/eFormAPI.Web ./eFormAPI.Web
COPY eform-angular-trashinspection-plugin/eFormAPI/Plugins/InsightDashboard.Pn ./InsightDashboard.Pn
RUN dotnet publish eFormAPI.Web -o eFormAPI.Web/out /p:Version=$GITVERSION --runtime linux-x64 --configuration Release
RUN dotnet publish InsightDashboard.Pn -o InsightDashboard.Pn/out /p:Version=$PLUGINVERSION --runtime linux-x64 --configuration Release

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/aspnet:3.1
WORKDIR /app
COPY --from=build-env /app/eFormAPI.Web/out .
RUN mkdir -p ./Plugins/InsightDashboard.Pn
COPY --from=build-env /app/InsightDashboard.Pn/out ./Plugins/InsightDashboard.Pn
COPY --from=node-env /app/dist wwwroot
RUN rm connection.json; exit 0

ENTRYPOINT ["dotnet", "eFormAPI.Web.dll"]
