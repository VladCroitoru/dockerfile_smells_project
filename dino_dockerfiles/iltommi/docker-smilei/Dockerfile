FROM fedora:latest

# install packages
RUN dnf -y update; \
    dnf install -y make gcc-c++ hdf5-openmpi hdf5-openmpi-devel openmpi-devel git which findutils python python-devel; \
    dnf install -y h5py ipython python2-pint python2-sphinx python2-matplotlib 

# build Smilei    
RUN source /etc/profile && module load mpi ;            \
    git clone https://github.com/SmileiPIC/Smilei.git ; \
    cd Smilei && make -j$(nproc) && make doc ;          \
    install smilei smilei_test /usr/local/bin

# create Smilei user    
RUN useradd -ms /bin/bash Smilei

# install happi for Smilei user
RUN su -c "cd /Smilei ; make happi" - Smilei

USER Smilei

WORKDIR /home/Smilei

