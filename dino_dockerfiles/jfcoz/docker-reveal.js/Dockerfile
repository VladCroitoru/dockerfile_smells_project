FROM debian:latest

# Install systems 
RUN apt-get update \
 && apt-get install -y \
        apt-transport-https \
        lsb-release \
        build-essential \
        curl \
        git \
        gnupg2 \
 && apt-get clean 

# Install node.js
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
 && apt-get install -y nodejs

# Install grunt
RUN npm install -g grunt-cli

# Install reveal.js
RUN git clone https://github.com/hakimel/reveal.js.git \
 && cd reveal.js \
 && npm install

COPY index.html /slides/
RUN rm /reveal.js/index.html
RUN ln -s /slides/index.html /reveal.js/index.html

COPY Gruntfile.js /reveal.js/

# Pandoc search for... 
# http://localhost:8000/reveal.js/css/reveal.min.css
# http://localhost:8000/reveal.js/js/reveal.min.js  
# http://localhost:8000/reveal.js/lib/js/head.min.js
# http://localhost:8000/reveal.js/css/print/pdf.css
# http://localhost:8000/reveal.js/css/theme/simple.css
# http://localhost:35729/livereload.js?snipver=1
# http://localhost:8000/reveal.js/css/theme/simple.css
# http://localhost:8000/reveal.js/css/print/pdf.css
# http://localhost:8000/reveal.js/plugin/zoom-js

RUN mkdir -p /pandoc/reveal.js/css/lib \
 && mkdir -p /pandoc/reveal.js/js \
 && mkdir -p /pandoc/reveal.js/lib/js \
 && mkdir -p /pandoc/reveal.js/css/print \
 && ln -s /reveal.js/css/reveal.css /pandoc/reveal.js/css/reveal.min.css \
 && ln -s /reveal.js/js/reveal.js /pandoc/reveal.js/js/reveal.min.js \
 && ln -s /reveal.js/lib/js/head.min.js /pandoc/reveal.js/lib/js/head.min.js \
 && ln -s /reveal.js/css/print/pdf.css /pandoc/reveal.js/css/print/pdf.css \
 && ln -s /reveal.js/css/theme/ /pandoc/reveal.js/css/theme \
 && ln -s /reveal.js/plugin /pandoc/reveal.js/plugin

RUN apt-get -y install pandoc

WORKDIR reveal.js 
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT /entrypoint.sh
EXPOSE 8000


