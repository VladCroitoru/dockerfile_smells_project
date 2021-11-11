FROM julia:0.4.2
MAINTAINER "Romain Pauli" gromainpauligmail.com
RUN apt-get update && \
    apt-get install -y curl cmake gettext gfortran pkg-config libgnutls28-dev sqlite3 \
    && rm -rf /var/lib/apt/lists/*
    
ENV JULIA_VER v0.4
ENV JULIA_PKG_DIR /root/.julia/${JULIA_VER}

RUN julia -e 'Pkg.update(); Pkg.add("Escher")'
RUN julia -e 'Pkg.add("Compose"); Pkg.add("Gadfly")'
RUN julia -e 'Pkg.add("SQLite"); Pkg.add("Roots")'
RUN julia -e 'Pkg.checkout("MacroTools")'

#RUN julia -e 'Pkg.update()'
#RUN julia -e 'Pkg.build()'

# RUN julia -e 'Pkg.checkout("Lazy"); Pkg.checkout("Patchwork"); Pkg.checkout("Mux")'
RUN ln -s ${JULIA_PKG_DIR}/Escher/bin/escher /usr/local/bin

RUN git clone http://github.com/l2omus/vinum-analytics.git usr/vinum-analytics
VOLUME ["/usr/vinum-analytics"]

EXPOSE 8080
WORKDIR usr/vinum-analytics
CMD escher --port 8080 --serve
