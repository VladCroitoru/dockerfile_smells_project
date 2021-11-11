FROM bitnami/minideb:jessie
# copy the contents of the `app/` folder into the container at build time
ADD app/ /app/
  
#run commands:
RUN apt-get update && apt-get install -y python3 python-dev python3-dev python-pip python-tk \ 
    && pip install virtualenv \
    # create a virtualenv we can later use
    && mkdir -p /venv/ \
    # install python version on virtual environment
    && virtualenv -p /usr/bin/python2.7 /venv \
    #activate virtual environment
    &&  /bin/bash -c "source /venv/bin/activate" \
    # install python dependencies into venv
    && /venv/bin/pip install -r /app/requirements.txt --upgrade \
    # clean cache
    && apt-get clean -y  \
    && apt-get autoclean -y  \
    && apt-get autoremove -y  \

    && rm -rf /usr/share/locale/*  \
    && rm -rf /var/cache/debconf/*-old  \
    && rm -rf /var/lib/apt/lists/*  \
    && rm -rf /usr/share/doc/*  \
      #set permission to task.sh
    && chmod +x /app/task.sh

ENV REDIS_SERVER redis.marathon.l4lb.thisdcos.directory
