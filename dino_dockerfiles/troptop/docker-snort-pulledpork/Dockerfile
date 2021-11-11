# Snort in Docker
FROM ubuntu:latest
ENV IPS false

RUN apt-get update && \
    apt-get install -y \
        wget \
        build-essential \
        # Pre-requisites for Snort DAQ (Data AcQuisition library)
        bison \
        flex \
        # Pre-Requisites for snort
        libpcap-dev \
        libpcre3-dev \
        libdumbnet-dev \
        # Additional required pre-requisite for Snort
        zlib1g-dev python-pip \
        # Optional libraries that improves fuctionality
        liblzma-dev inotify-tools supervisor \
        openssl iptables libnghttp2-dev libnetfilter-queue-dev libnetfilter-queue1 libnfnetlink-dev libnfnetlink0 \
        libssl-dev libcrypt-ssleay-perl liblwp-useragent-determined-perl git vim tzdata python-jinja2 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install supervisor-stdout
# Define working directory.
WORKDIR /opt

ENV DAQ_VERSION 2.0.6
RUN wget https://www.snort.org/downloads/snort/daq-${DAQ_VERSION}.tar.gz \
    && tar xvfz daq-${DAQ_VERSION}.tar.gz \
    && cd daq-${DAQ_VERSION} \
    && ./configure; make; make install

ENV SNORT_VERSION 2.9.11.1
RUN wget https://www.snort.org/downloads/snort/snort-${SNORT_VERSION}.tar.gz \
    && tar xvfz snort-${SNORT_VERSION}.tar.gz \
    && cd snort-${SNORT_VERSION} \
    && ./configure --enable-sourcefire --enable-perfprofiling --enable-linux-smp-stats --enable-gre  --enable-targetbased --enable-mpls \
    &&  make && make install

RUN ldconfig

# ENV SNORT_RULES_SNAPSHOT 2972
# ADD snortrules-snapshot-${SNORT_RULES_SNAPSHOT} /opt
RUN mkdir -p /var/log/snort && \
    mkdir -p /usr/local/lib/snort_dynamicrules && \
    mkdir -p /etc/snort && \
    mkdir -p /opt/log && \
    mkdir -p /etc/pulledpork
ADD mysnortrules /etc/snort
ADD mypulledpork /etc/pulledpork

RUN /bin/chmod +x /etc/pulledpork/pulledpork.pl && /bin/ln -s /etc/pulledpork/pulledpork.pl /usr/local/bin/pulledpork.pl && \
    echo '01 04 * * * /usr/local/bin/pulledpork.pl -c /etc/pulledpork/pulledpork.conf -l' >> /etc/crontab 
    #restart cron
# Clean up APT when done.
RUN apt-get clean && rm -rf /tmp/* /var/tmp/* \
    /opt/snort-${SNORT_VERSION}.tar.gz /opt/daq-${DAQ_VERSION}.tar.gz

# Validate an installation

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY rotatesnort.conf /etc/logrotate.d/rotatesnort.conf
COPY copy-file.sh .
COPY jinja-pulledpork-conf.py .
COPY pulledpork-template.conf .
COPY jinja-snort-conf.py .
COPY snort-template.conf .
COPY entrypoint.sh /opt/
RUN chmod +x /opt/entrypoint.sh /opt/copy-file.sh 
CMD ["/usr/bin/supervisord"]
