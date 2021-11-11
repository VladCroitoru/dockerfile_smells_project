FROM thomasp85/firedock_test

ARG root='/'
ENV FIERY_ROOT=$root

ADD firedock /firedock

RUN R -e "devtools::install_local('firedock/')"

## Switch from root
RUN useradd --create-home --shell /bin/bash ruser
USER ruser
WORKDIR /home/ruser


EXPOSE 8080

CMD Rscript -e 'firedock::get_app()$ignite()'
