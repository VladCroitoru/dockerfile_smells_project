# Second Stage
FROM microsoft/dotnet:1.1.2-runtime
EXPOSE 5000

ENV ASPNETCORE_URLS=http://+:5000
ENV ASPNETCORE_ENVIRONMENT=Production
ADD dist /app/
WORKDIR /app
CMD ["dotnet", "ProIdeas.UI.dll"]