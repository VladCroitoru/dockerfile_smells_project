FROM alpine
MAINTAINER Kailash Peri <perik@us.ibm.com>

RUN apk add --update --no-cache curl bash \
    && rm -rf /var/cache/apk/* \
    && /usr/bin/curl -L https://clis.ng.bluemix.net/download/bluemix-cli/latest/linux64 --output /bx.tar.gz \
    && tar xvf /bx.tar.gz \
    && rm -rf /bx.tar.gz \
    && chmod +x /Bluemix_CLI/bin/bluemix \
    && chmod +x /Bluemix_CLI/bin/cfcli/cf \
    && ln -s /Bluemix_CLI/bin/bluemix /usr/local/bin/bx \
    && ln -s /Bluemix_CLI/bin/cfcli/cf /usr/local/bin/cf \
    && /usr/local/bin/bx config --check-version false 

COPY  login2CloudEnv.sh / 

RUN chmod +x /login2CloudEnv.sh

CMD bash -C '/login2CloudEnv.sh'; bash
