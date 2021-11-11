FROM bitnami/minideb:jessie
 
MAINTAINER rbravo@datiobd.com

#ENVIRONMENT VARIABLES
ENV master=localhost
ENV redis_server=localhost
ENV redis_key=key
ENV docker_task=cirobarradov/executor-app
ENV task_cpu=0.5
ENV task_mem=100
# copy the contents of the `app/` folder into the container at build time
ADD pymesos/ /pymesos/
# copy the contents of the `app/` folder into the container at build time
ADD app/ /app/

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
CMD ["sh", "-c", "/app/scheduler.sh $master $redis_server $redis_key $docker_task $task_cpu $task_mem"]
