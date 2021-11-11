FROM i386/ubuntu:14.04
LABEL maintainer cseelye@gmail.com

# Add the prerequisites to the container
# Installing firefox is an aweful hack, but it's an easy way to get all of the GTK and X11 stuff that the webex tools need
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        firefox \
        libpangox-1.0-0 \
        libpangoxft-1.0-0 \
        wget \
        x11-utils && \
    apt-get autoremove && \
    apt-get clean && \
    rm --force --recursive /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Add the webex tools to the container
RUN wget --no-verbose http://support.webex.com/supportutilities/nbr2mp4.tar && \
    tar xf nbr2mp4.tar && \
    chmod +x nbr2mp4.sh && \
    echo "/" | ./nbr2mp4.sh && \
    rm -f nbr2mp4.sh nbr2mp4.tar

WORKDIR /nbr2_mp4
ENTRYPOINT ["./nbr2mp4"]
