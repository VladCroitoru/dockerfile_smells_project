FROM ubuntu:14.04
RUN touch /bin/irpf-2017
RUN echo "#!/usr/bin/env bash" > /bin/irpf-2017; \
    echo "[ ! -d /usr/local/IRPF2017/ ] && ./IRPF2017Linux-x86_64v1.1.bin" >> /bin/irpf-2017; \
    echo "/usr/bin/java -Xms128M -Xmx512M -jar /usr/local/IRPF2017/irpf.jar" >> /bin/irpf-2017; \
    chmod u+x /bin/irpf-2017; \
    apt-get update; \
    apt-get install -y openjdk-7-jdk; \
    apt-get install -y wget
RUN wget http://downloadirpf.receita.fazenda.gov.br/irpf/2017/irpf/arquivos/IRPF2017Linux-x86_64v1.1.bin; \
    chmod u+x IRPF2017Linux-x86_64v1.1.bin; \    
    mkdir /root/shared