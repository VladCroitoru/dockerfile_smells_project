FROM tozd/runit

EXPOSE 27017/tcp
EXPOSE 5432/tcp

ENV METEOR_ALLOW_SUPERUSER=true

RUN apt-get update -q -q
RUN locale-gen --no-purge en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN apt-get install curl mongodb postgresql postgresql-server-dev-9.3 python-pip python-dev numactl git --yes --force-yes
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.3/main/postgresql.conf
RUN echo 'hostssl all all 0.0.0.0/0 md5' >> /etc/postgresql/9.3/main/pg_hba.conf
RUN sed -i 's/peer/trust/g' /etc/postgresql/9.3/main/pg_hba.conf
RUN sed -i 's/md5/trust/g' /etc/postgresql/9.3/main/pg_hba.conf
RUN curl https://install.meteor.com | /bin/sh

COPY ./etc /etc

RUN mkdir -p /benchmark
WORKDIR /benchmark

RUN git clone https://github.com/mitar/peerdb-benchmark.git -b postgresql-python peerdb-benchmark-postgresql-python
RUN git clone https://github.com/mitar/peerdb-benchmark.git -b mongodb-python peerdb-benchmark-mongodb-python
RUN git clone https://github.com/mitar/peerdb-benchmark.git -b mongodb-meteor peerdb-benchmark-mongodb-meteor
RUN git clone https://github.com/mitar/peerdb-benchmark.git -b master peerdb-benchmark

RUN pip install -r peerdb-benchmark-mongodb-python/requirements.txt
RUN pip install -r peerdb-benchmark-postgresql-python/django_project/requirements.txt

WORKDIR /benchmark/peerdb-benchmark-mongodb-meteor

RUN meteor build . --directory

WORKDIR /benchmark/peerdb-benchmark/generate_jsons

RUN mkdir -p /benchmark/jsons
RUN python generate_jsons.py base_param.json /benchmark/jsons/ SIZE 10 100 1000 10000 100000
RUN python generate_jsons.py base_param.json /benchmark/jsons/ NUMBER 1 2 4 6 8 10

WORKDIR /benchmark
