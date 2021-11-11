FROM postgres:13

RUN apt-get update && \
    apt-get -y install python3 postgresql-plpython3-13 python3-pip

RUN apt-get install -y git make && \
    git clone https://github.com/gavinwahl/postgres-json-schema.git && \
    cd postgres-json-schema && \
    make install && \
    cd .. && \
    rm -rf postgres-json-schema

RUN pip3 install -U pip wheel && \
    pip3 install requests pyjwt[crypto] boto3

WORKDIR /src
COPY . /src
