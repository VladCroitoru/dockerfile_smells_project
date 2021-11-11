FROM nginx:1.13.6-alpine

LABEL maintainer="Hung Nguyen <nmhung1210@gmail.com>"

ENV NGINX_AMPLIFY_VERSION 1.0.0

# API_KEY is required for configuring the NGINX Amplify Agent.
# It could be your real API key for NGINX Amplify here if you wanted
# to build your own image to host it in a private registry.
# However, including private keys in the Dockerfile is not recommended.
# Use the environment variables at runtime as described below.

ENV API_KEY 1234567890

# If AMPLIFY_IMAGENAME is set, the startup wrapper script will use it to
# generate the 'imagename' to put in the /etc/amplify-agent/agent.conf
# If several instances use the same 'imagename', the metrics will
# be aggregated into a single object in NGINX Amplify. Otherwise Amplify
# will create separate objects for monitoring (an object per instance).
# AMPLIFY_IMAGENAME can also be passed to the instance at runtime as
# described below.

ENV AMPLIFY_IMAGENAME "<imagename>"

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
        ca-certificates \
        wget \
        python \
        python-dev \
        py-configobj \
        git \
        util-linux \
        procps \
        gcc \
        musl-dev \
        linux-headers && \
        wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \
            python get-pip.py --ignore-installed --user && \
            ~/.local/bin/pip install setuptools --upgrade --user && \
            rm -rf nginx-amplify-agent && \
            git clone "https://github.com/nginxinc/nginx-amplify-agent" && \
            cd nginx-amplify-agent && \
            ~/.local/bin/pip install --upgrade \
                --target=amplify --no-compile \
                -r packages/requirements && \
            python setup.py install && \
            cp nginx-amplify-agent.py /usr/bin && \
            mkdir -p /var/log/amplify-agent && \
            chmod 755 /var/log/amplify-agent && \
            mkdir -p /var/run/amplify-agent && \
            chmod 755 /var/run/amplify-agent && \
            rm -rf ~/.local && \
            apk del \
                ca-certificates \
                wget \
                python-dev \
                py-configobj \
                git \
                gcc \
                musl-dev \
                linux-headers &&\
                rm -rf /var/cache/apk/* &&\
                mkdir -p /etc/amplify-agent


COPY ./conf.d/agent.conf /etc/amplify-agent/agent.conf
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh; \
    chmod +r /proc;

# TO set/override API_KEY and AMPLIFY_IMAGENAME when starting an instance:
# docker run --name my-nginx1 -e API_KEY='..effc' -e AMPLIFY_IMAGENAME="service-name" -d nmhung1210/nginx-alpine-amplify

ENTRYPOINT ["/entrypoint.sh"]
