FROM debian:jessie
MAINTAINER Robin Hübner "profan@prfn.se"

ENV hostname "cdn.prfn.se"
RUN apt-get update && apt-get install -y --no-install-recommends vsftpd
RUN apt-get clean

RUN echo "seccomp_sandbox=NO" >> /etc/vsftpd.conf
RUN echo "pasv_address="$hostname >> /etc/vsftpd.conf
RUN echo "pasv_addr_resolve=YES" >> /etc/vsftpd.conf
RUN echo "pasv_enable=YES" >> /etc/vsftpd.conf
RUN echo "port_enable=NO" >> /etc/vsftpd.conf
RUN echo "pasv_min_port=10000" >> /etc/vsftpd.conf
RUN echo "pasv_max_port=10100" >> /etc/vsftpd.conf
RUN echo "tcp_wrappers=YES" >> /etc/vsftpd.conf
RUN echo "anon_root=/var/ftp" >> /etc/vsftpd.conf
RUN echo "anon_max_rate=0" >> /etc/vsftpd.conf
RUN echo "force_dot_files=YES" >> /etc/vsftpd.conf
RUN sed -i "s/listen=NO/listen=YES/" /etc/vsftpd.conf
RUN sed -i "s/listen_ipv6=YES/listen_ipv6=NO/" /etc/vsftpd.conf
RUN sed -i "s/connect_from_port_20=YES/connect_from_port_20=NO/" /etc/vsftpd.conf
RUN sed -i "s/local_enable=YES/local_enable=NO/" /etc/vsftpd.conf
RUN sed -i "s/anonymous_enable=NO/anonymous_enable=YES/" /etc/vsftpd.conf

RUN mkdir -p /var/run/vsftpd/empty
VOLUME /var/ftp

EXPOSE 20 21
EXPOSE 10000-10100

CMD /usr/sbin/vsftpd
