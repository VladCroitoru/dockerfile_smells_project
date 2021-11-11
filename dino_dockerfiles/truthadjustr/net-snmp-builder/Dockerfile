FROM truthadjustr/ubuntu1:latest

RUN apt-get install libperl-dev file \
    && mkdir /net-snmp  \
    && wget --no-check-certificate https://sourceforge.net/projects/net-snmp/files/net-snmp/5.7.3/net-snmp-5.7.3.tar.gz \
    && tar xf net-snmp-5.7.3.tar.gz -C /net-snmp/ \
    && rm -f /net-snmp-5.7.3.tar.gz

WORKDIR /net-snmp/
