FROM centos:7

RUN set -e \
	&& rm -f /etc/yum.repos.d/CentOS-Base.repo

ADD CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo

RUN set -e \
	&& yum upgrade -y \
	&& yum update -y \
	&& yum install -y kernel-devel kernel-headers readline-devel zlib-develi \
	&& yum groupinstall "Development Tools" -y

WORKDIR /root

RUN set -e \
	&& git clone https://github.com/riywo/anyenv ~/.anyenv \
	&& echo 'export PATH="$HOME/.anyenv/bin:$PATH"' >> ~/.bashrc \
	&& echo 'eval "$(anyenv init -)"' >> ~/.bashrc

RUN set -e \
	&& yum clean all

CMD ["bash", "--login"]
