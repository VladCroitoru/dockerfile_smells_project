FROM phusion/baseimage:0.9.18

MAINTAINER Luke Campbell <luke.campbell@rpsgroup.com>

RUN apt-get update && apt-get install -y \
      git \
      libssl-dev \
      libxml2-dev \
      libxslt1-dev \
      libpq-dev \
      python-dev \
      redis-tools \
      wget \
      python-pip
COPY contrib/install_python.sh /install_python.sh
RUN /install_python.sh
RUN rm -rf /var/lib/apt/lists/*
RUN pip install -U pip
RUN mkdir /opt/catalog-harvesting
COPY MANIFEST.in setup.py README.rst requirements.txt requirements_ext.txt LICENSE \
     /opt/catalog-harvesting/
# TODO: ideally put external git dependency handling in setup.py under
# `dependency_links`
RUN pip install -r /opt/catalog-harvesting/requirements_ext.txt && \
    pip install -r /opt/catalog-harvesting/requirements.txt && \
    pip install gunicorn
COPY catalog_harvesting /opt/catalog-harvesting/catalog_harvesting
COPY contrib/conf/logging.json /opt/catalog-harvesting/
RUN pip install -e /opt/catalog-harvesting

RUN useradd -m harvest
RUN mkdir /var/log/harvest
RUN chown harvest:harvest /var/log/harvest
COPY ./contrib/my_init.d /etc/my_init.d
COPY ./contrib/run_web.sh ./contrib/run_worker.py /
VOLUME ["/data"]
ENV OUTPUT_DIR /data
EXPOSE 3000

CMD ["/sbin/my_init", "--", "/run_web.sh"]
