#FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
COPY ./src /src
WORKDIR /src

#release to target folder
RUN dotnet publish point-cloud-analyzer-web -o /publish --configuration Release

#FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 
FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS runtime
WORKDIR /app

COPY --from=build /publish .

RUN dpkg --add-architecture i386 && \
	apt-get update && \
	apt-get install -y wget gnupg software-properties-common unzip zenity && \
	wget -O - https://dl.winehq.org/wine-builds/winehq.key | apt-key add - && \
	add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main' && \
	wget -nv https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04/Release.key -O Release.key && \
	apt-key add - < Release.key && \
	apt-add-repository 'deb https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04/ ./' && \
	apt-get update && \
	apt install -y --install-recommends winehq-stable && \
	wget  https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks && \
	chmod +x winetricks 

ENTRYPOINT ["dotnet", "point-cloud-analyzer-web.dll", "--environment=Development"]