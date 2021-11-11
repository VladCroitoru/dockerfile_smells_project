FROM andybalaam/apache
MAINTAINER Andy Balaam <andybalaam@artificialworlds.net>

# Enable non-free for the spectrum-roms package :-(
RUN \
    perl -p -i -e 's/main/main non-free/' /etc/apt/sources.list

# Install the bas2tap utility
RUN \
    apt-get update && \
    apt-get install -y \
        git \
        gcc \
        make \
    && \
    git clone https://github.com/andybalaam/bas2tap.git && \
    cd bas2tap && \
    make

# The packages that are used at runtime
RUN \
    apt-get install -y \
        fuse-emulator-sdl \
        spectrum-roms \
        xvfb

# Patch xvfb-run so it works inside a CGI script -
# instead of "wait || :" (which I don't understand)
# we just "sleep 0.2" before checking whether the
# Xvfb process started OK.
COPY xvfb-run.patch /
RUN \
    apt-get install -y patch && \
    patch /usr/bin/xvfb-run < /xvfb-run.patch && \
    rm /xvfb-run.patch

# Useful if you make run-interactive
RUN apt-get install -y vim

# Clean packages that aren't needed at runtime
RUN \
    apt-get remove -y \
        git \
        gcc \
        make \
        patch \
    && \
    apt-get autoremove -y && \
    apt-get clean

# Apache config
COPY spectrum-basic.conf /etc/apache2/conf-available/
RUN /bin/ln -sf /etc/apache2/conf-available/spectrum-basic.conf /etc/apache2/conf-enabled/
RUN /bin/ln -sf /etc/apache2/mods-available/cgi.load            /etc/apache2/mods-enabled/
RUN /bin/ln -sf /etc/apache2/mods-available/actions.conf        /etc/apache2/mods-enabled/
RUN /bin/ln -sf /etc/apache2/mods-available/actions.load        /etc/apache2/mods-enabled/

# The magic that makes Spectrum BASIC run as CGI
COPY spectrum-basic.cgi  /usr/lib/cgi-bin/

# Example basic programs
COPY hello.basic /var/www/html/
COPY hello-name.basic /var/www/html/

# Useful if you make run-interactive
COPY startapache /

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

