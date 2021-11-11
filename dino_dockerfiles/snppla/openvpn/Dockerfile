from debian

RUN apt-get update
RUN apt-get -y install openvpn

ADD openvpn_init.sh /sbin/
RUN chmod +x /sbin/openvpn_init.sh

CMD /sbin/openvpn_init.sh
