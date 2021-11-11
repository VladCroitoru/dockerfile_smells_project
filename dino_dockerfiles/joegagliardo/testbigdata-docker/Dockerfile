FROM joegagliardo/ubuntu
MAINTAINER joegagliardo
ENV MSSQL_SA_PASSWORD='SaPassword17!' 
ENV MSSQL_PID='evaluation'
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add - && \
    add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2017.list)"  && \
    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add - && \
    add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/16.04/prod.list)" && \
    apt-get update && \
    apt-get install -y mssql-server mssql-server-fts && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools unixodbc-dev && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc && \
    echo '#! /bin/sh' > /ss-accept.sh && \
    echo "ACCEPT_EULA=Y MSSQL_SA_PASSWORD=$MSSQL_SA_PASSWORD MSSQL_PID=$MSSQL_PID /opt/mssql/bin/mssql-conf -n setup accept-eula" >> /ss-accept.sh && \
    chmod +x /ss-accept.sh
    



