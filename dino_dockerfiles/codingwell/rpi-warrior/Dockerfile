# Dockerfile for Raspberry Pi
FROM codingwell/rpi-raspbian-qemu
RUN [ "cross-build-start" ]

# Set environment variables.
ENV HOME /root

# Install dependencies
RUN apt-get update \
 && apt-get install -y python-pip git sudo python-software-properties wget liblua5.1-0 \
 && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD get-wget-lua.sh /

RUN apt-get update \
 && apt-get install -y libssl-dev liblua5.1-0-dev autoconf flex pkg-config bzip2 gcc make \
 && chmod +x /get-wget-lua.sh && bash -c "/get-wget-lua.sh" \
 && apt-get purge -y libssl-dev liblua5.1-0-dev autoconf flex pkg-config bzip2 gcc make \
 && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Fix dnsmasq bug (see https://github.com/nicolasff/docker-cassandra/issues/8#issuecomment-36922132)
RUN echo 'user=root' >> /etc/dnsmasq.conf

# Setup system for the warrior
RUN useradd warrior
RUN echo "warrior ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN mkdir /home/warrior && chown warrior: /home/warrior

# Clone warrior code
RUN (cd /home/warrior && git clone -b docker https://github.com/ArchiveTeam/warrior-code2.git && chown -R warrior:warrior warrior-code2)

# Expose web interface port
EXPOSE 8001

# Add the warrior service entry for runit
ADD bootpi.sh /home/warrior/bootpi.sh

CMD ["/home/warrior/bootpi.sh"]

RUN [ "cross-build-end" ]