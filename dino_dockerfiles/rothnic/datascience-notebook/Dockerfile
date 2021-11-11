FROM rothnic/anaconda-notebook
MAINTAINER Nick Roth "nlr06886@gmail.com"

# R dependencies from conda
COPY src/install_r.sh /tmp/install_r.sh
RUN /tmp/install_r.sh

# R ipython kernel setup
COPY src/setup_r.sh /tmp/setup_r.sh
COPY src/kernel.json /tmp/kernel.json
RUN /tmp/setup_r.sh

USER condauser
EXPOSE 8888
