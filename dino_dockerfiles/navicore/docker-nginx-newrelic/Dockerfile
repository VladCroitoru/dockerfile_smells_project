FROM buildpack-deps:jessie-curl

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo 'deb http://nginx.org/packages/debian/ jessie nginx' >> /etc/apt/sources.list
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y nginx-nr-agent && \
    rm -rf /var/lib/apt/lists/*

COPY start.sh /opt/
COPY nginx-nr-agent.ini /etc/nginx-nr-agent/
CMD /opt/start.sh
