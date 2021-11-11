FROM fedora
WORKDIR /root
EXPOSE 22
CMD /sshd.sh
ADD sshd.sh /sshd.sh
RUN : \
 && dnf update -y \
 && dnf install -y \
      openssh-server \
      ca-certificates \
      hg \
      git \
      make \
      python \
 && dnf groupinstall -y "C Development Tools and Libraries" \
 && dnf groupinstall -y "Development Tools" \
 && dnf groupinstall -y "RPM Development Tools" \
 && hg clone http://hg.openjdk.java.net/jdk9/dev jdk9-dev \
 && cd jdk9-dev \
 && bash get_source.sh \
 && :
