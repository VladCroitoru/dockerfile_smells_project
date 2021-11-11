# docker build -t telminov/park-worker-p3 .
# docker run --rm -ti --name parkworker3 --link parkkeeper --volume=/var/docker/park-worker-p3/conf/:/conf/ telminov/park-worker-p3

FROM telminov/ubuntu-14.04-python-3.5
MAINTAINER telminov <telminov@soft-way.biz>

# settings
VOLUME /conf/

RUN apt-get update && \
    apt-get install -y \
                    vim \
                    build-essential

# install
COPY . /opt/park-worker-p3
WORKDIR /opt/park-worker-p3
RUN pip3 install -e .

WORKDIR /opt/park-worker-p3/parkworker3

CMD test "$(ls /conf/settings.py)" || cp settings.sample.py /conf/settings.py; \
    rm settings.py; \
    ln -s /conf/settings.py settings.py; \
    python3 bin/start_workers.py
