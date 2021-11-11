FROM debian:8

# install required commands
RUN apt-get update && apt-get install -y  wget expect spamassassin

# Enable SpamAssassin to be started from sysvinit
RUN sed "s/ENABLED=0/ENABLED=1/" /etc/default/spamassassin > /tmp/spamassassin ;\
    mv /tmp/spamassassin /etc/default/spamassassin

# copy files for axigen installer
COPY axigen/ /axigen
COPY bin/	/usr/local/bin

# install axigen with default settings and set to start at boot
# 	admin password 		= admin
# 	postmaster password = postmaster
RUN cd /axigen ;\
    wget https://www.axigen.com/usr/files/axigen-10.1.4/axigen-10.1.4.amd64.deb.run ;\
    export TERM=xterm ;\
    chmod +x /axigen/* /usr/local/bin/axigen.sh /usr/local/bin/entrypoint.sh;\
    /axigen/install-axigen.exp ;\
    cd / ;\
    rm -r /axigen

#expose required ports for SMTP, POP3, IMAP, POP3S, IMAPS, WebAdmin, Webmail and CLI
EXPOSE 25 110 143 993 995 9000 80 7000

# set mountpoint for axigen datafiles
VOLUME ["/var/axigen"]

# Entrypoint for the container
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# cmd to start the service when the container starts
CMD ["/usr/local/bin/axigen.sh"]
