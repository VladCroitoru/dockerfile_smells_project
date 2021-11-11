
#FROM python:3.4
FROM python:3.6.9

#Install SQL ODBC driver (Debian Buster)
#https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017#microsoft-odbc-driver-17-for-sql-server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
        && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update \
        && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 \
        && echo "SQL-ODBC Driver Ready"

RUN mkdir /code
WORKDIR /code

#Turbodbc Requirements 
#https://turbodbc.readthedocs.io/en/latest/pages/getting_started.html#installation
RUN apt-get update \
        && apt-get install -y --no-install-recommends dialog \
        && apt-get update \
        && apt-get install -y --no-install-recommends libboost-all-dev \
        && apt-get install -y --no-install-recommends python-dev \
        && apt-get install -y --no-install-recommends unixodbc-dev \
        && echo "Turbodbc Req Done"

#Install Python Modules requiered by turbodbc
RUN pip install -U numpy pybind11

#Install App Python Modules
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
	&& apt-get install -y --no-install-recommends openssh-server \
	&& echo "$SSH_PASSWD" | chpasswd 

COPY sshd_config /etc/ssh/
COPY init.sh /usr/local/bin/
	
RUN chmod u+x /usr/local/bin/init.sh
EXPOSE 5000 2222
ENTRYPOINT ["init.sh"]
