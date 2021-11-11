FROM reszelaz/leap-systemd

RUN zypper ar -f http://download.opensuse.org/repositories/home:/cmft/openSUSE_Leap_42.1 cmft
RUN zypper --no-gpg-checks refresh cmft

# install:
# vim - for easy editing of text files
# xorg-x11-fonts - apparently necessary to run jive
# glibc-locale is necessary for the en_US locale setting (tangosys user needs it)
RUN zypper install -y tango-db tango-test tango-java python-sardana vim \
    xorg-x11-fonts glibc-locale

ENV TERM=xterm

EXPOSE 10000
