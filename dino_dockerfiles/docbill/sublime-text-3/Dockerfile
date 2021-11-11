FROM fedora
MAINTAINER Bill C Riemers https://github.com/docbill

ARG URL=https://download.sublimetext.com/sublime_text_3_build_3103_x64.tar.bz2
RUN dnf update -y && \
	dnf install -y git sudo curl wget bzip2 tar libX11 gtk2-devel PackageKit-gtk3-module libcanberra-gtk2 libcanberra-gtk3 firefox && \
	dnf clean -y all

RUN wget --quiet --output-document=/tmp/sublime-text.tar.bz2 "$URL" && \
	(cd /opt ; tar xvvfj /tmp/sublime-text.tar.bz2) && \
	rm -f /tmp/sublime-text.tar.bz2 && \
	ln -s /opt/sublime_text/sublime_text  /usr/bin/subl && \
        ln -s /opt/sublime_text_3 /opt/sublime_text

ADD Dockerfile /Dockerfile
ADD subl-wrapper /usr/local/bin/subl-wrapper

RUN chmod 555 /usr/local/bin/subl-wrapper

VOLUME /workspace
ENV HOME=/workspace DISPLAY=:0 LC_ALL=en_US.UTF-8
WORKDIR /workspace

ENTRYPOINT ["/usr/local/bin/subl-wrapper"]

