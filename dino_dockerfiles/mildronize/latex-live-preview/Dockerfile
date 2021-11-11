FROM debian:jessie
MAINTAINER Thada Wangthammang <mildronize@gmail.com>

# Add for local build
# ADD sources.list /etc/apt/sources.list

# Install texlive curl pip3
RUN apt-get -y update && \
    apt-get install -y --fix-missing \
                    curl \
                    texlive \
                    python3-pip && \
    apt-get -yq autoremove && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
# Install mildronize/latex-live-preview
RUN pip3 install watchdog
RUN mkdir /app
RUN curl -o /app/watchdog_latex -O https://raw.githubusercontent.com/mildronize/latex-live-preview/master/bin/watchdog_latex
RUN curl -o /app/topdf -O https://raw.githubusercontent.com/mildronize/latex-live-preview/master/bin/topdf
RUN chmod a+x /app/watchdog_latex
RUN chmod a+x /app/topdf

WORKDIR /src
VOLUME /src
