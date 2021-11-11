# VERSION   0.1
FROM        debian:unstable
MAINTAINER  Paul R. Tagliamonte <paultag@hylang.org>

RUN apt-get update && apt-get install -y \
    python3.4 \
    python3-pip \
    python3-distro-info \
    python3-setuptools \
    python-setuptools \
    python-dput \
    dput-ng \
    git subversion \
    dpkg-dev \
    devscripts

RUN python3.4 /usr/bin/pip3 install -e \
        git://git.debian.org/collab-maint/dputng.git#egg=dput

# TODO fix the Hy tip issues so we can use Hy from master again
#RUN python3.4 /usr/bin/pip3 install -e \
#        git://github.com/hylang/hy.git#egg=hy

COPY requirements.txt /opt/pault.ag/crank/
WORKDIR /opt/pault.ag/crank
RUN python3.4 /usr/bin/pip3 install -r requirements.txt

COPY bin/crank /usr/bin/crank
ENV CRANK_HOME /crank/

# add a user to run crank as, for better safeness
ENV HOME /home/user
RUN groupadd user && useradd -d "$HOME" -m -g user user
RUN mkdir -p "$CRANK_HOME" && chown -R user:user "$CRANK_HOME"
# (add a "crank_home" dput target, for easy local testing ♥)
RUN { echo '{'; echo '  "method": "local",'; echo '  "allow_unsigned_uploads": true,'; echo '  "incoming": "'"$CRANK_HOME"'"'; echo '}'; } > /etc/dput.d/profiles/crank_home.json
USER user

ENTRYPOINT ["/usr/bin/crank"]
CMD []

COPY . /opt/pault.ag/crank
