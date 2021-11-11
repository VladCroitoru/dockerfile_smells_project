FROM totem/totem-base:trusty-1.0.1
 
RUN apt-get update --fix-missing && \ 
    apt-get upgrade -y && \
    apt-get install -y libevent1-dev python3-dev python3 python3-pip  && \
    apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

ENTRYPOINT ["python3"]
CMD ["--version"]
