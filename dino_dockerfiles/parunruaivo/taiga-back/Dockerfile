FROM python:latest
MAINTAINER Parun Rua Ivo <parunruaivo@gmail.com>

ENV TAIGA_HOME=/home/taiga \
    TAIGA_RUNTIME_DIR=/runtime \
    C_FORCE_ROOT=true \
    LANG=en_US.UTF-8 \
    LC_TYPE=en_US.UTF-8

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends --no-install-suggests -y \
            locales \
            build-essential \
            binutils-doc \
            autoconf \
            flex \
            bison \
            libjpeg-dev \
            libfreetype6-dev \
            zlib1g-dev \
            libzmq3-dev \
            libgdbm-dev \
            libncurses5-dev \
            automake \
            libtool \
            libffi-dev \
            curl \
            git \
            tmux \
            gettext \
    && pip install circus gunicorn \
    && rm -rf /var/lib/apt/lists/*


RUN git clone -b stable --single-branch https://github.com/taigaio/taiga-back.git ${TAIGA_HOME}/taiga-back

RUN useradd -d ${TAIGA_HOME} taiga

COPY assets/locale.gen /etc/locale.gen

WORKDIR ${TAIGA_HOME}/taiga-back

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install taiga-contrib-slack

COPY assets/templates/settings.py ${TAIGA_HOME}/taiga-back/settings/local.py
COPY assets/templates/checkdb.py ${TAIGA_RUNTIME_DIR}/checkdb.py
COPY assets/templates/initial_user.json ${TAIGA_HOME}/taiga-back/taiga/users/fixtures/initial_user.json

RUN mkdir ${TAIGA_HOME}/conf ${TAIGA_HOME}/logs

COPY assets/circus/circus.ini ${TAIGA_HOME}/conf/circus.ini
COPY assets/circus/circus.conf /etc/init/circus.conf

RUN echo "LANG=en_US.UTF-8" > /etc/default/locale
RUN echo "LC_TYPE=en_US.UTF-8" >> /etc/default/locale
RUN echo "LC_MESSAGES=POSIX" >> /etc/default/locale
RUN echo "LANGUAGE=en" >> /etc/default/locale

RUN locale-gen en_US.UTF-8

COPY assets/runtime ${TAIGA_RUNTIME_DIR}/

COPY docker-entrypoint.sh /sbin/docker-entrypoint.sh

RUN chmod +x /sbin/docker-entrypoint.sh

EXPOSE 8000

CMD ["/sbin/docker-entrypoint.sh"]
