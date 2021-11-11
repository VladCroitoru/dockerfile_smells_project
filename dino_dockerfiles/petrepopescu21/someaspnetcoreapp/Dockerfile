FROM microsoft/aspnetcore-build:2.0 AS buildstep

WORKDIR /app

COPY . .

RUN dotnet restore
RUN dotnet publish -c Release -o out



FROM microsoft/aspnetcore:2.0

WORKDIR /app

COPY --from=buildstep /app/out .

EXPOSE 80

ENTRYPOINT [ "dotnet", "somenetcoreapp.dll" ]