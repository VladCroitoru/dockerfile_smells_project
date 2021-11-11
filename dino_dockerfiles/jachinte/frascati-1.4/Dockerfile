# FraSCAti 1.4
#
# VERSION 0.1.0

FROM jachinte/oracle-jdk-1.6.0_23:0.1.0

MAINTAINER Miguel Jiménez <migueljimenezachinte@gmail.com>
LABEL Description="This image provides FraSCAti 1.4 running with Oracle JDK 1.6.0_23. \
It uses an enhanced version of the FraSCAti binaries. You can read more about \
that at https://github.com/jachinte/frascati-binaries" \
      License="MIT" \
      Usage="docker run --rm -ti jachinte/frascati-1.4 frascati --version" \
      Version="0.1.0"

# Install dependencies.
RUN apt-get -y update && apt-get install -y \
    unzip \
    wget

# Install and configure FraSCAti.
ADD frascati-1.4-bin.zip /tmp
RUN unzip /tmp/frascati-1.4-bin.zip -d /opt/

# Update the FraSCAti binary.
RUN wget https://raw.githubusercontent.com/jachinte/frascati-binaries/master/frascati
RUN mv frascati /opt/frascati-runtime-1.4/bin/
RUN chmod a+x /opt/frascati-runtime-1.4/bin/frascati

# Set environment variables.
ENV FRASCATI_HOME /opt/frascati-runtime-1.4
ENV PATH $PATH:$FRASCATI_HOME/bin

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
