# Use official Ubuntu release
FROM ubuntu:latest

# Maintainer
LABEL maintainer="Björn Gernert <mail@bjoern-gernert.de>"

# Update Ubuntu image
RUN apt-get -qq update && apt-get -qq upgrade

# Install Kerberos Server
RUN apt-get -qq install krb5-kdc krb5-admin-server

# Clean up updates/install
RUN apt-get -qq autoclean && apt-get -qq autoremove && apt-get -qq clean

# Set environment variables
ENV REALM ${REALM:-EXAMPLE.COM}
ENV SUPPORTED_ENCRYPTION_TYPES ${SUPPORTED_ENCRYPTION_TYPES:-aes256-cts-hmac-sha1-96:normal}
ENV KADMIN_PRINCIPAL ${KADMIN_PRINCIPAL:-root/admin}
ENV KADMIN_PASSWORD ${KADMIN_PASSWORD:-HSIeb8334Jsc375woW}
ENV KDC_HOSTNAME ${KDC_HOSTNAME:-kerberos.example.com}

# Export volumes
VOLUME /dev/urandom:/dev/random
VOLUME /kerberos

# Copy scripts and configurations files into container
ADD start_kerberos /root/start_kerberos

# Allow execution of start script
RUN chmod u+x /root/start_kerberos

# Set config environment
RUN echo "export KRB5_CONFIG=/kerberos/krb5.conf" >> /root/.bashrc
RUN echo "export KRB5_KDC_PROFILE=/kerberos/krb5kdc/kdc.conf" >> /root/.bashrc

# Make Kerberos ports available
EXPOSE 88
EXPOSE 464
EXPOSE 749
EXPOSE 750

# Start Kerberos
CMD ["/root/start_kerberos"]