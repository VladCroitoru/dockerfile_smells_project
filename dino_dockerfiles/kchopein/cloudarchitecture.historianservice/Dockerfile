FROM microsoft/aspnetcore:2.0
WORKDIR /app
EXPOSE 5000
COPY ./publish .
ENTRYPOINT ["dotnet", "HistorianService.dll"]