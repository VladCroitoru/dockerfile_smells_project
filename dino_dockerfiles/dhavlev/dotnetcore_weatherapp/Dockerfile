FROM centos:latest

RUN yum -y install libunwind libicu && curl -sSL -o dotnet.tar.gz https://go.microsoft.com/fwlink/?linkid=848821 && mkdir -p /opt/dotnet && tar zxf dotnet.tar.gz -C /opt/dotnet && ln -s /opt/dotnet/dotnet /usr/local/bin

RUN yum -y install httpd

COPY weather.conf /etc/httpd/conf.d/weather.conf

COPY MicroServiceDocker MicroServiceDocker

COPY apachestart.sh MicroServiceDocker/apachestart.sh

COPY dotnetstart.sh MicroServiceDocker/dotnetstart.sh

COPY entry.sh MicroServiceDocker/entry.sh

RUN dotnet restore MicroServiceDocker

RUN dotnet publish MicroServiceDocker/MicroServiceDocker.csproj -c Release -o published


WORKDIR /MicroServiceDocker

#CMD ./entry.sh

ENTRYPOINT ["./entry.sh"]

#RUN dotnet WeatherMicroservice.dll --server.urls http://127.0.0.1:5000

#ENTRYPOINT ["dotnet", "WeatherMicroservice.dll", "--server.urls", "http://127.0.0.1:5000"]

#ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]
