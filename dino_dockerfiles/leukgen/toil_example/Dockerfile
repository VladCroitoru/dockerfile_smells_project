FROM python:3.8-slim-buster

RUN \
    # install packages dependencies
    apt update -yqq && \
    apt install -yqq \
        curl \
        git \
        locales \
        wget && \
    apt clean && \
    \
    # configure locale, see https://github.com/rocker-org/rocker/issues/19
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.utf8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8

# set locales
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

# mount the output volume as persistant
ENV OUTPUT_DIR /data
VOLUME ${OUTPUT_DIR}

# install toil_example
COPY . /code
RUN pip install /code && rm -rf /code

# add entry point
ENTRYPOINT ["toil_example"]
