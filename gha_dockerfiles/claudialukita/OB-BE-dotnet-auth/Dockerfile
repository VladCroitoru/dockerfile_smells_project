#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster as build
WORKDIR /app
EXPOSE 80
EXPOSE 443

# copy csproj and restore as distinct layers
COPY *.sln .
COPY OB-BE-dotnet-auth/*.csproj ./OB-BE-dotnet-auth/
COPY BLL/*.csproj ./BLL/
COPY DAL/*.csproj ./DAL/

#restore dependencies
RUN dotnet restore

# copy everything else and build app
COPY OB-BE-dotnet-auth/ ./OB-BE-dotnet-auth/
COPY BLL/ ./BLL/
COPY DAL/ ./DAL/

#
WORKDIR /app/OB-BE-dotnet-auth
RUN dotnet publish -c Release -o out 
#
FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS runtime
WORKDIR /app 
#
COPY --from=build /app/OB-BE-dotnet-auth/out ./
ENTRYPOINT ["dotnet", "API.dll"]