#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM arm32v7/ubuntu:20.04 AS deps
RUN apt-get update;
RUN apt-get install -y wget
WORKDIR /usr/share/dotnet
WORKDIR /usr/share
RUN wget https://download.visualstudio.microsoft.com/download/pr/2178c8a1-ad48-4e51-9ddd-4e3ab64d1f0e/68746abefadf62be43ca525653c915a1/dotnet-sdk-3.1.405-linux-arm.tar.gz -O /usr/share/sdk.tar.gz
RUN tar zxf /usr/share/sdk.tar.gz -C /usr/share/dotnet
ENV DOTNET_ROOT=/usr/share/dotnet
ENV PATH="$PATH:/usr/share/dotnet"
WORKDIR /vendor
RUN apt-get install -y git
RUN git clone --depth 1 --branch 4.5.4 https://github.com/emgucv/emgucv
WORKDIR /vendor/emgucv
RUN git submodule update --init --recursive
WORKDIR /vendor/emgucv/platforms/ubuntu/20.04
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get install -y sudo
RUN sed -s 's/sudo apt-get install/sudo apt-get install libgstreamer1.0-dev/g' ./apt_install_dependency
RUN sed -s 's/-DBUILD_opencv_python3:BOOL=FALSE/-DBUILD_opencv_python3:BOOL=FALSE -DWITH_GSTREAMER:BOOL=TRUE/g' ./cmake_configure
RUN yes | ./apt_install_dependency
RUN ./cmake_configure

FROM deps as emgucv
WORKDIR /libs
COPY --from=deps /vendor/emgucv/libs .
RUN mv arm/* .
ENV LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/libs"
ENV SUDO_FORCE_REMOVE=yes
RUN apt remove -y sudo git wget
RUN apt-get clean autoclean
RUN apt-get autoremove --yes
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/
RUN rm -rf /vendor/emgucv
RUN rm /usr/share/sdk.tar.gz

FROM deps AS build
WORKDIR /src
COPY ["NVs.OccupancySensor.API/NVs.OccupancySensor.API.csproj", "NVs.OccupancySensor.API/"]
COPY ["NVs.OccupancySensor.CV/NVs.OccupancySensor.CV.csproj", "NVs.OccupancySensor.CV/"]
RUN dotnet restore "NVs.OccupancySensor.CV/NVs.OccupancySensor.CV.csproj"
RUN dotnet restore "NVs.OccupancySensor.API/NVs.OccupancySensor.API.csproj"
COPY . .
WORKDIR "/src/NVs.OccupancySensor.API"
RUN dotnet build "NVs.OccupancySensor.API.csproj" -c Release -o /app/build -r linux-arm 

FROM build AS test
RUN dotnet test --no-build

FROM build AS publish
RUN dotnet publish "NVs.OccupancySensor.API.csproj" -c Release -o /app/publish -r linux-arm

FROM emgucv AS final
WORKDIR /app
ENV ASPNETCORE_URLS=http://+:80
ENV ASPNETCORE_ENVIRONMENT=Production
EXPOSE 80
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "NVs.OccupancySensor.API.dll"]