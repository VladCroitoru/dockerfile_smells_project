FROM debian
MAINTAINER Dusty Wilson <dusty.wilson@scjalliance.com>
LABEL description="PaperCut MF Server"

RUN useradd -mUd /papercut -s /bin/bash papercut
WORKDIR /papercut

RUN mkdir -p /papercut/server/data \
    && chown -R papercut:papercut /papercut
VOLUME /papercut/server/data

EXPOSE 9191 9192 9193

RUN apt-get update \
    && apt-get install -y \
       cpio \
       cups \
       cups-daemon \
       curl \
       samba \
       wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /installer \
    && cd /installer \
    && wget -O pcmf-setup.sh $(curl https://www.papercut.com/products/mf/upgrade-available/ | grep https | grep -v link_previous | cut -d'"' -f2 | grep -Ei "pcmf-setup-[0-9\.]+-linux-x64\.sh" | awk '{sub(/^.*\?http=/, "", $1)}{sub(/\.sh.*?$/, ".sh", $1)}{print $1}' | sed -e's/%\([0-9A-F][0-9A-F]\)/\\\\\x\1/g' | xargs echo -e) \
    && chmod 755 pcmf-setup.sh

COPY run.sh /papercut/
RUN chmod 755 /papercut/run.sh

ENTRYPOINT ["./run.sh"]
CMD ["default"]


# [Run notes:]
#
# Run a normal app server:
# docker run -it --rm -p 9191:9191 -p 9192:9192 -p 9193:9193 scjalliance/papercut-mf
#
# Run a site server:
# docker run -it --rm -p 9191:9191 -p 9192:9192 -p 9193:9193 scjalliance/papercut-mf site-server


# [Distribution notes:]
#
# From the pcmf-setup-15.3.34420-linux-x64.sh README-LINUX.txt file
# downloaded via https://cdn.papercut.com/files/mf/15.x/pcmf-setup-15.3.34420-linux-x64.sh
# by this Dockerfile's maintainer on Saturday, February 13, 2016:
#
# > This evaluation version may be distributed unchanged and in complete form by a
# > 3rd Party.
#
# We accept this as permission to distribute the installer as part of
# a Docker image.  You will note that we do not make any modification
# to PaperCut's installer image, but instead simply pull it straight
# from their website, then assist with the installation within a
# Docker container after it has been started within the end consumer
# hosting environment.  If PaperCut disapproves, they're welcome to
# communicate with the maintainer of this Dockerfile listed above.
