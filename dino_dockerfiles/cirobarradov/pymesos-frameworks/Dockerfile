FROM bitnami/minideb:jessie
 
MAINTAINER rbravo@datiobd.com

# expose port
#EXPOSE $PORTS

# copy the contents of the `app/` folder into the container at build time
ADD pymesos/ /pymesos/
# copy the contents of the `app/` folder into the container at build time
ADD app/ /app/
ADD app2/ /app2/
ADD app2/config /app2/config

#run commands:
RUN apt-get update && apt-get install -y python3 python-dev python3-dev python-pip libzookeeper-mt-dev \ 
    && pip install virtualenv \
    # create a virtualenv we can later use
    && mkdir -p /venv/ \
    # install python version on virtual environment
    && virtualenv -p /usr/bin/python2.7 /venv \
    #activate virtual environment
    &&  /bin/bash -c "source /venv/bin/activate" \
    # install redis python cli
    && /venv/bin/pip install redis \
    # install python dependencies into venv
    && /venv/bin/pip install -r /pymesos/requirements.txt --upgrade \
    && /venv/bin/pip install /pymesos/lib/pymesos-0.2.13.tar.gz \
    # clean cache
    && apt-get clean -y  \
    && apt-get autoclean -y  \
    && apt-get autoremove -y  \

    && rm -rf /usr/share/locale/*  \
    && rm -rf /var/cache/debconf/*-old  \
    && rm -rf /var/lib/apt/lists/*  \
    && rm -rf /usr/share/doc/*

RUN chmod a+x /app/scheduler.sh
RUN chmod a+x /app2/scheduler.sh

ENV MASTER 172.16.48.181
ENV DOCKER_TASK cirobarradov/executor-app
ENV MAX_TASKS 5
ENV REDIS_SERVER redis.marathon.l4lb.thisdcos.directory

# CMD source /venv/bin/activate
