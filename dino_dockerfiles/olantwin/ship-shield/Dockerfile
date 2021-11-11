FROM scr4t/ship-base:13.03.2017

ENV FAIRSHIP_COMMIT 5129f65f63e7dcfa696c9b0cd7b285779ea7953d
ENV OPTIMISATION_COMMIT 7a2a97802f6b4811169f6e286bf1cfc14057aed4

RUN yum -y install yum-plugin-ovl \
        python2-pip \
        && yum -y autoremove \
        && find /usr/share/locale | grep -v en | xargs rm -rf \
        && yum clean all

RUN /bin/bash -l -c "\
        rm -rf opt/FairShipRun /opt/FairShip &&\
        git clone -b optimisation_shield https://github.com/olantwin/FairShip.git /opt/FairShip  &&\
        cd /opt/FairShip &&\
        git checkout $FAIRSHIP_COMMIT &&\
        mkdir -p /opt/FairShip/../FairShipRun &&\
        cd /opt/FairShip/../FairShipRun &&\
        cmake /opt/FairShip -DCMAKE_INSTALL_PREFIX=$(pwd) -DCMAKE_CXX_COMPILER=$(/opt/FairSoftInst/bin/fairsoft-config --cxx) -DCMAKE_C_COMPILER=$(/opt/FairSoftInst/bin/fairsoft-config --cc) &&\
        make"

RUN /bin/bash -l -c "\
        git clone -b disneyland https://github.com/olantwin/muon_shield_optimisation.git /code &&\
        cd /code &&\
        git checkout $OPTIMISATION_COMMIT"

RUN /bin/bash -l -c "\
        source /opt/FairShipRun/config.sh &&\
        pip install $(grep Cython /code/requirements.txt) &&\
        pip install $(grep numpy /code/requirements.txt) &&\
        pip install -r /code/requirements.txt"
