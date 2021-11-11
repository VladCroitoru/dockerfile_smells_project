FROM debian:jessie
MAINTAINER François Billant <fbillant@gmail.com>

RUN sed -i.bak 's/jessie main/jessie main contrib non-free/g' /etc/apt/sources.list

ADD run.sh /usr/bin/run.sh
RUN chmod +x /usr/bin/run.sh

RUN export DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get install -y \
git \
python-pip \
iptables

RUN cd /usr/src && \
git clone https://github.com/fail2ban/fail2ban.git && \
cd fail2ban && \
pip install .

# The use of this script is temporary due to https://github.com/fail2ban/fail2ban/issues/1107 - See in the script for more details
CMD ["/usr/bin/run.sh"]
