# Epigenome Browser mm9 CM

FROM bgruening/hicbrowser

MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com

RUN conda install -y bx-python -c bioconda -c conda-forge
RUN apt-get update && apt-get install -y npm node

RUN cd /home/hicbrowser/conda/lib/python2.7/site-packages/hicbrowser/client && \
    npm install grunt-cli && \
    npm i && npm install handlebars underscore && \
    ln -s  /usr/bin/nodejs /usr/sbin/node -f && \
    ./node_modules/grunt-cli/bin/grunt dist

COPY ./img/header.png /home/hicbrowser/conda/lib/python2.7/site-packages/hicbrowser/static/img/banner.png
COPY ./img/logo_sfb992.png /home/hicbrowser/conda/lib/python2.7/site-packages/hicbrowser/static/img/logo_sfb992.png
COPY ./img/logo_uni.png /home/hicbrowser/conda/lib/python2.7/site-packages/hicbrowser/static/img/logo_uni.png
COPY ./index.hbs /home/hicbrowser/conda/lib/python2.7/site-packages/hicbrowser/client/templates/index.hbs
COPY ./index.html /home/hicbrowser/conda/lib/python2.7/site-packages/hicbrowser/client/html/index.html

RUN cd /home/hicbrowser/conda/lib/python2.7/site-packages/hicbrowser/client && ./node_modules/grunt-cli/bin/grunt dist

EXPOSE 80

# Mark folders as imported from the host.
VOLUME ["/data/"]

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
