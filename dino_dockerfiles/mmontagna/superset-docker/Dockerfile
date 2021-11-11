FROM debian:stretch
MAINTAINER Marco Montagna <marcojoemontagna@gmail.com>

# Configure environment
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONPATH=/home/superset:/etc/superset:$PYTHONPATH \
    SUPERSET_HOME=/home/superset

RUN mkdir $SUPERSET_HOME /etc/superset
WORKDIR $SUPERSET_HOME

RUN useradd -U -m superset && \
    chown -R superset:superset /etc/superset && \
    chown -R superset:superset ${SUPERSET_HOME} && \
    apt-get update && \
    apt-get install -y \
        git \
        build-essential \
        curl \
        default-libmysqlclient-dev \
        libffi-dev \
        libldap2-dev \
        libpq-dev \
        libsasl2-dev \
        libssl-dev \
        openjdk-8-jdk \
        python-dev \
        python-pip && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*

COPY requirements.txt $SUPERSET_HOME
RUN pip install --no-cache-dir -r $SUPERSET_HOME/requirements.txt

COPY superset_config.py /etc/superset
COPY entry_point.sh $SUPERSET_HOME
COPY superset_version $SUPERSET_HOME

RUN pip install git+https://github.com/apache/incubator-superset.git@`cat superset_version`

EXPOSE 8088
ENTRYPOINT ["/home/superset/entry_point.sh"]
CMD ["superset", "runserver"]
USER superset