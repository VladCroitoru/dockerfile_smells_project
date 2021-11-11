FROM mongo

RUN apt-get update && apt-get install -y \
				python \
				python-dev \
				gcc \
				curl \
				unzip \
				libffi-dev \
	&& rm -rf /var/lib/apt/lists/*

# Add Consul from https://releases.hashicorp.com/consul
ENV CONSUL_VER 0.6.4
ENV CONSUL_CHECKSUM abdf0e1856292468e2c9971420d73b805e93888e006c76324ae39416edcf0627

RUN curl --retry 7 -Lso /tmp/consul.zip "https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_linux_amd64.zip" \
    && echo "${CONSUL_CHECKSUM}  /tmp/consul.zip" | sha256sum -c \
    && unzip /tmp/consul -d /usr/local/bin \
    && rm /tmp/consul.zip \
    && mkdir /config

# Add Consul template
# Releases at https://releases.hashicorp.com/consul-template/
ENV CONSUL_TEMPLATE_VER 0.14.0
ENV CONSUL_TEMPLATE_CHECKSUM 7c70ea5f230a70c809333e75fdcff2f6f1e838f29cfb872e1420a63cdf7f3a78

RUN curl --retry 7 -Lso /tmp/consul-template.zip \
        "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VER}/consul-template_${CONSUL_TEMPLATE_VER}_linux_amd64.zip" \
    && echo "${CONSUL_TEMPLATE_CHECKSUM}  /tmp/consul-template.zip" | sha256sum -c \
    && unzip /tmp/consul-template.zip -d /usr/local/bin \
    && rm /tmp/consul-template.zip

# Add Containerpilot and set its configuration
ENV CONTAINERPILOT_VER 2.3.0
ENV CONTAINERPILOT_CHECKSUM 0b2dc36172248d0df3b73ad67c3262ed49096e6c1204e2325b3fd7529617f130

RUN curl --retry 7 -Lso /tmp/containerpilot.tar.gz \
         "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VER}/containerpilot-${CONTAINERPILOT_VER}.tar.gz" \
    && echo "${CONTAINERPILOT_CHECKSUM}  /tmp/containerpilot.tar.gz" | sha256sum -c \
    && tar xzf /tmp/containerpilot.tar.gz -C /usr/local/bin \
    && rm /tmp/containerpilot.tar.gz

# get Python drivers MySQL, Consul, and Manta
RUN curl -Ls -o get-pip.py https://bootstrap.pypa.io/get-pip.py \
	&& python get-pip.py	&& pip install \
				PyMongo==3.2.2 \
				python-Consul==0.4.7 \
				manta==2.5.0 \
				mock==2.0.0

# configure ContainerPilot and MySQL
COPY etc /etc
COPY bin /usr/local/bin

# override the parent entrypoint
ENTRYPOINT []

CMD [ \
	"containerpilot", \
	"mongod", \
	"--replSet=joyent" \
]
