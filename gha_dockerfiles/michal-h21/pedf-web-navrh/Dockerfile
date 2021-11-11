FROM michalh21/lettersmith

RUN luarocks install h5tk 
RUN luarocks install date

ARG HTML_DIR 
ARG WWW_DIR
ARG DATA_DIR
ENV HTML_DIR /opt/html/
ENV WWW_DIR /opt/www/result/
ENV DATA_DIR /opt/data/

WORKDIR /opt/pedf_web/
COPY *.lua ./
COPY lib/ ./lib/
COPY trans/ ./trans/
COPY templates/ ./templates/

ENTRYPOINT ["lua", "web.lua"]
