FROM dockerfile/python 
RUN pip install librabbitmq kombu 

RUN apt-get update
RUN apt-get install -y --force-yes smbclient cifs-utils
RUN mkdir -p /koppelvlak/orcaexports

RUN mkdir /src
WORKDIR /src
COPY src /src

RUN chmod a+rx run.sh
CMD ["/src/run.sh"]
