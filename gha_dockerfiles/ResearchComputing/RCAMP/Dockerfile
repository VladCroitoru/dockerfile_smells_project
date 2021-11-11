FROM centos:8
MAINTAINER Aaron Holt <aaron.holt@colorado.edu>

RUN dnf -y install epel-release && \
    dnf -y install wget dpkg

# Install gosu to drop user and chown shared volumes at runtime
RUN export GOSU_VERSION=1.10 && \
  	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \
  	wget -O /usr/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" && \
  	wget -O /tmp/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" && \
  	export GNUPGHOME="$(mktemp -d)" && \
  	gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 && \
  	gpg --batch --verify /tmp/gosu.asc /usr/bin/gosu && \
  	rm -rf "$GNUPGHOME" /tmp/gosu.asc && \
  	chmod +x /usr/bin/gosu; \
  	gosu nobody true && \
    unset GOSU_VERSION

# Install core dependencies
RUN dnf -y update && \
    dnf -y groupinstall "Development Tools" && \
    dnf -y install epel-release curl which wget && \
    dnf -y install sssd pam-devel openssl-devel pam_radius && \
    dnf -y install python3 python3-devel python3-pip && \
    dnf -y install openldap-devel mysql-devel pcre pcre-devel sqlite

# Remove uneeded extras
RUN dnf -y remove wget dpkg && \
    dnf clean all

WORKDIR /opt
ENV VIRTUAL_ENV=/opt/rcamp_venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /opt/
RUN pip3 install --upgrade pip && \
    pip3 install wheel && \
    pip3 install -r requirements.txt

RUN git clone -b python3 https://github.com/ResearchComputing/django-ldapdb-test-env
WORKDIR /opt/django-ldapdb-test-env
RUN python3 setup.py install
WORKDIR /opt

# Add uwsgi conf
COPY uwsgi.ini /opt/uwsgi.ini

# Add codebase to container
COPY rcamp /opt/rcamp

WORKDIR /opt/rcamp
# Set gosu entrypoint and default command
COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["sh","/usr/local/bin/docker-entrypoint.sh"]
CMD ["/opt/rcamp_venv/bin/uwsgi", "/opt/uwsgi.ini"]
