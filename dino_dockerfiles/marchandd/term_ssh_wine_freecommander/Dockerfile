FROM marchandd/term_ssh_root_wine:latest
MAINTAINER Marchand D. https://github.com/marchandd/term_ssh_wine_freecommander
ENV VE_version="MarchandD_20151117_v02.01" 
# Downloads softwares deliveries from file (-i) to target directories (-P) with log (-o)
COPY scripts/*.txt /root/Downloads/
RUN wget -i /root/Downloads/downloadsLinks.txt -P /root/Downloads -o /root/Downloads/downloadsLinks.log
RUN chmod 755 /root/Downloads/*.exe
# Copy install scripts from local to /usr/local/sbin
COPY scripts/*.sh /usr/local/sbin/
RUN chmod 755 /usr/local/sbin/*.sh
WORKDIR /root
RUN ln -s /usr/local/sbin/ software_install_directory
# Directory ready for SSH
WORKDIR /etc/supervisor