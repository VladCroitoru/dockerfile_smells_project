FROM mcr.microsoft.com/dotnet/sdk:5.0
WORKDIR /src
EXPOSE 5000
EXPOSE 5001
COPY . .
RUN cd ChatApp.API && dotnet dev-certs https --trust
CMD cd ChatApp.API && dotnet run
