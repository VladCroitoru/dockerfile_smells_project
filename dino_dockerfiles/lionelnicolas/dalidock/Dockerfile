FROM ubuntu:focal-20210713 as python-build

# environment variables
ENV \
	LC_ALL=C.UTF-8 \
	LANG=C.UTF-8 \
	LANGUAGE=C.UTF-8 \
	DEBIAN_FRONTEND=noninteractive

# install packages
RUN \
	echo "deb http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse"           >/etc/apt/sources.list && \
	echo "deb http://security.ubuntu.com/ubuntu focal-security main restricted universe multiverse" >>/etc/apt/sources.list && \
	echo "deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse"  >>/etc/apt/sources.list && \
	apt-get update && \
	apt-get install -y --no-install-recommends \
		build-essential \
		libvirt-dev \
		pkg-config \
		python3 \
		python3-dev \
		python3-venv \
		python3-wheel \
		twine \
		virtualenv \
		wget \
		&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists

# install pip
RUN \
	cd /tmp && \
	wget http://bootstrap.pypa.io/get-pip.py && \
	python3 ./get-pip.py && \
	rm -rfv *

# install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN \
	pip3 install \
		--requirement /tmp/requirements.txt \
		--ignore-installed \
		--target /tmp/packages

FROM ubuntu:focal-20210713 as base

# environment variables
ENV \
	LC_ALL=C.UTF-8 \
	LANG=C.UTF-8 \
	LANGUAGE=C.UTF-8 \
	DEBIAN_FRONTEND=noninteractive

# install packages
RUN \
	echo "deb http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse"           >/etc/apt/sources.list && \
	echo "deb http://security.ubuntu.com/ubuntu focal-security main restricted universe multiverse" >>/etc/apt/sources.list && \
	echo "deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse"  >>/etc/apt/sources.list && \
	apt-get update && \
	apt-get install -y --no-install-recommends \
		bind9-host \
		ca-certificates \
		dirmngr \
		dnsmasq \
		dnsutils \
		ed \
		gpg \
		gpg-agent \
		haproxy \
		inotify-tools \
		iproute2 \
		libvirt0 \
		net-tools \
		python3 \
		python3-distutils \
		runit \
		wget \
		&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists && \
	rm -vf /etc/ssh/ssh_host_*

# install tini
RUN \
	TINI_VERSION=v0.19.0 && \
	http_proxy='' gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0527A9B7 && \
	wget -O/usr/bin/tini     "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" && \
	wget -O/usr/bin/tini.asc "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc" && \
	gpg --verify /usr/bin/tini.asc && \
	rm -f /usr/bin/tini.asc && \
	chmod a+x /usr/bin/tini

# add python packages
COPY --from=python-build /tmp/packages /usr/lib/python3/dist-packages

# add scripts
ADD entrypoint dalidock haproxy-start /usr/sbin/

# add configuration scripts
ADD etc /etc/

# set entrypoint
ENTRYPOINT ["/usr/sbin/entrypoint"]
