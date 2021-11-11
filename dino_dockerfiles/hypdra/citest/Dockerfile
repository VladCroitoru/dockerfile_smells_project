FROM microsoft/aspnetcore-build:1.0-1.1
WORKDIR /app

COPY . ./
RUN dotnet restore ./CIWorkflow.sln && dotnet publish ./CIWorkflow.sln -c Release -o out
EXPOSE 80
ENTRYPOINT ["dotnet", "out/CIWorkflow.dll"]
