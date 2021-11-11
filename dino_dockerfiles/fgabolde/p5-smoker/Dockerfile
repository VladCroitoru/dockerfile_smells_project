FROM rancher/jenkins-swarm:v0.1.0
MAINTAINER Fabrice Gabolde <fabrice.gabolde@gmail.com>

USER root

RUN apt-get update && apt-get install -y --no-install-recommends bzip2 patch perlbrew cpanminus

RUN perlbrew install-cpanm

RUN perlbrew init
RUN echo ". /root/perl5/perlbrew/etc/bashrc" >> /root/.bash_profile
RUN echo ". /root/perl5/perlbrew/etc/bashrc" >> /var/jenkins_home/.bash_profile && chown jenkins: /var/jenkins_home/.bash_profile

# pre-downloaded tarballs
COPY dists /root/perl5/perlbrew/dists
COPY expected-perl-dists.txt /tmp/

RUN ["/bin/bash", "-c", "perlbrew install-multiple --notest -j2 perl-5.23.7 perl-5.22.1 perl-5.20.3 perl-5.18.4 perl-5.16.3 perl-5.14.4 perl-5.12.5 perl-5.10.1 perl-5.8.9"]

# perlbrew (at least 0.66 from jessie) returns success even if some
# perls did not install properly
RUN ["/bin/bash", "-c", "perlbrew list | sed -e 's/^..//' | sort | diff /tmp/expected-perl-dists.txt -"]

# our customized version
COPY ./run.sh /run.sh

# as per jenkins-swarm
ENTRYPOINT ["/run.sh"]
