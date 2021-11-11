FROM microsoft/mssql-server-linux:latest

RUN apt-get update && apt-get install -y python sudo

ENV SA_PASSWORD=yourStrong123Password
ENV ACCEPT_EULA=Y

RUN /opt/mssql/bin/sqlservr-setup --accept-eula --set-sa-password

RUN \
locale-gen en_US.UTF-8 && \
update-locale && \
apt-get update && \
apt-get install -y curl apt-transport-https && \
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
curl https://packages.microsoft.com/config/ubuntu/15.10/prod.list | tee /etc/apt/sources.list.d/msprod.list && \
apt-get update && \
apt-get install -y mssql-tools

# sqlcmd has a version suffix
RUN cd /bin && ln -s $(find /opt/mssql-tools/bin -name sqlcmd*) sqlcmd
EXPOSE 1433