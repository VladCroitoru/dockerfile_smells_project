FROM python:2.7

RUN pip install psutil pymongo numpy matplotlib python-dateutil PrettyTable mongoengine pyyaml dargparse \
    && pip install -e git+git://github.com/rueckstiess/mtools.git@develop#egg=mtools \
    && pip install --no-deps git+git://github.com/srault95/mongodb-tools.git@refresh#egg=mongodbtools \
    && pip install git+git://github.com/mrsarm/mongotail.git@master#egg=mongotail \
    && pip install --no-deps git+git://github.com/mongolab/dex.git@master#egg=dex

RUN curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.2.7.tgz \
    && tar -xzf mongodb-linux-x86_64-3.2.7.tgz \
    && mv mongodb-linux-x86_64-3.2.7/bin/* /usr/local/bin \
    && rm -rf mongodb-linux-x86_64-3.2.7* /usr/local/bin/mongod /usr/local/bin/mongos

VOLUME /data

WORKDIR /data