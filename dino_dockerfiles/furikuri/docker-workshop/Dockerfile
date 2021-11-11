FROM alpine:3.4

RUN apk update && \
    apk upgrade && \
    apk add \
          nodejs \
          python \
          python-dev \
          musl-dev \
          libffi-dev \
          openssl-dev \
          py-pip \
          gcc \
          git \
          g++ \
          git \
          vim \
          docker && \
    pip install --upgrade pip && \
    pip install libsass && \
    pip install butterfly

RUN git clone https://github.com/hakimel/reveal.js.git /opt/revealjs
RUN git clone https://github.com/docker-training/docker-present.git /opt/docker-present
RUN git clone https://github.com/docker-training/presentations.git /opt/docker-presentations
RUN git clone https://github.com/denehyg/reveal.js-menu.git /opt/revealjs/plugin/menu
RUN git clone https://github.com/paradoxxxzero/butterfly /opt/butterfly

RUN npm install -g http-server

WORKDIR /opt/revealjs

RUN mkdir -p /opt/revealjs/css/print/

RUN cp /opt/docker-present/present/css/docker.css /opt/revealjs/css/theme/
RUN cp /opt/docker-present/present/css/docker-code.css /opt/revealjs/lib/css/
RUN cp /opt/docker-present/present/css/sd_custom.css /opt/revealjs/css/
RUN cp -R /opt/docker-present/present/css/print /opt/revealjs/css/print/
RUN cp -R /opt/docker-present/present/fonts /opt/revealjs/fonts/
RUN cp -R /opt/docker-present/present/images /opt/revealjs/images/
RUN cp /opt/docker-presentations/modules/welcome-module-dockercon2016/images/title_slide_dockercon2016.png /opt/revealjs/images/

COPY profile /root/.profile
COPY presentation/index.html /opt/revealjs/index.html
COPY presentation/images /opt/revealjs/images
COPY docker_start.sh /opt/revealjs/start.sh
COPY butterfly.sass /opt/butterfly/butterfly/sass/main.sass
RUN sassc /opt/butterfly/butterfly/sass/main.sass > /opt/butterfly/butterfly/static/main.css

EXPOSE 3000 57575
CMD [ "./start.sh" ]