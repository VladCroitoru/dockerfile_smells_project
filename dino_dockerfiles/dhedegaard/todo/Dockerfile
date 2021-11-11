FROM microsoft/dotnet:2.1-sdk

COPY todo /app

WORKDIR /app

RUN ["dotnet", "restore"]

RUN ["dotnet", "build"]

RUN ["dotnet", "publish", "-c", "Release"]

EXPOSE 5000/tcp

CMD ["dotnet", "run", "bin/Release/netcoreapp2.1/todo.dll", "-c", "Release"]
