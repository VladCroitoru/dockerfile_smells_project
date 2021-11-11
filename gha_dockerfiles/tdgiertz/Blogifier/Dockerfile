FROM mcr.microsoft.com/dotnet/sdk:5.0 as base

COPY ./ /opt/blogifier
WORKDIR /opt/blogifier

RUN ["dotnet","publish","./src/Blogifier/Blogifier.csproj","-c","Release","-o","./outputs" ]

FROM mcr.microsoft.com/dotnet/aspnet:5.0 as run
COPY --from=base /opt/blogifier/outputs /opt/blogifier/outputs
WORKDIR /opt/blogifier/outputs
ENTRYPOINT ["dotnet", "Blogifier.dll"]
