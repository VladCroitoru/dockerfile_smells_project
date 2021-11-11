FROM nginx:stable

WORKDIR /opt

RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install sigal

COPY run.sh sigal.conf.py auth.conf auth.htpasswd ./

ENV LANG C.UTF-8

CMD ["./run.sh"]
