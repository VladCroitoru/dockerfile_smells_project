
FROM multiarch/debian-debootstrap:amd64-stretch

# Install packages
RUN apt-get update \
    && apt-get install -y jq tzdata python3 python3-dev python3-pip \
        python3-six python3-pyasn1 libportaudio2 alsa-utils \
    && pip3 install --upgrade pip \
    && pip3 install --upgrade google-assistant-library google-auth \
        requests_oauthlib cherrypy flask flask-jsonpify flask-restful \
        grpcio google-assistant-grpc google-auth-oauthlib \
    && apt-get remove -y --purge python3-pip python3-dev \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

   
   
# Copy data
COPY run.sh /
COPY *.py /

RUN chmod a+x /run.sh

VOLUME /data
COPY *.json /data/
EXPOSE 9324
EXPOSE 5000

ENTRYPOINT [ "/run.sh" ]