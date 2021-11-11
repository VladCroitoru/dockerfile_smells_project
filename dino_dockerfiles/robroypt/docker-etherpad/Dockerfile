FROM node:0.10

RUN apt-get update && \
    apt-get install -y gzip git curl python libssl-dev mysql-client && \
    rm -r /var/lib/apt/lists/*

RUN cd /opt && \
    git clone https://github.com/ether/etherpad-lite && \
    cd etherpad-lite && \
    bin/installDeps.sh && \
    rm settings.json

RUN cd /opt/etherpad-lite && 
    npm install \
        ep_font_color \
        ep_font_family \
        ep_font_size \
        ep_headings2 \
        ep_hide_line_numbers \
        ep_hide_referrer \
        ep_horizontal_line \
        ep_page_ruler \
        ep_tables2
    
COPY entrypoint.sh /entrypoint.sh
VOLUME /opt/etherpad-lite/var

RUN ln -s /opt/etherpad-lite/var/settings.json /opt/etherpad-lite/settings.json

WORKDIR /opt/etherpad-lite
EXPOSE 9001
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bin/run.sh", "--root"]
