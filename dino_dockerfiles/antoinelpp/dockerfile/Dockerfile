############################################################
# Dockerfile to build LPPic
# Based on Fedora base image
############################################################

# Set the base image from jeandet
FROM jeandet/teamcity-docker-minimal-agent
LABEL maintainer "Antoine Tavant <antoine.tavant@lpp.polytechnique.fr>"

# Update the repository sources list
#RUN dnf -y update

################## BEGIN INSTALLATION ######################

RUN dnf install -y git openmpi-devel cmake hdf5-openmpi-devel petsc-openmpi-devel hypre* gcc-gfortran module-macros gcc-c++ zlib-devel wget
RUN dnf -y install redhat-rpm-config python3-devel python3-tkinter


RUN echo "system.lppic=true" >> /opt/buildagent/conf/buildAgent.dist.properties

#--------------------------------------------------------------
                 #LD_LIBRARY_PATH
#--------------------------------------------------------------
RUN export LD_LIBRARY_PATH=/usr/lib64/openmpi/lib/
ENV PATH=${PATH}:/usr/lib64
    #HDF5_INCLUDE=/usr/lib64/openmpi/include
    #HDF5_LIB=/usr/lib64/gfortran/modules/openmpi/
    #PETSC_DIR
    #HYPRE_DIR

######################
## Env variables for LPPic compilation
######################
# RUN export HDF5_DIR=/usr/lib64/openmpi/
ENV HDF5_INCLUDE=/usr/lib64/gfortran/modules/openmpi/
ENV HDF5_LIB=/usr/lib64/openmpi/lib
ENV HYPRE_INCLUDE=/usr/include/openmpi-x86_64/hypre
ENV HYPRE_LIB=/usr/lib64/openmpi/lib
ENV PETSC_INCLUDE=/usr/include/openmpi-x86_64/petsc
ENV PETSC_LIB=/usr/lib64/openmpi/lib
ENV COMP=mpifort

######################
## Env variables for LPPic execution with OpenMPI in Dockers
## from https://github.com/open-mpi/ompi/issues/4948
######################
ENV OMPI_MCA_btl_vader_single_copy_mechanism=none

# RUN module load mpi/openmpi-x86_64  # does not work ??


###########################
##       Install LPPview for results post-processing
##########################
RUN pip3 install numpy matplotlib h5py scipy astropy ffmpy plasmapy pandas tqdm

RUN git clone --recursive https://hephaistos.lpp.polytechnique.fr/rhodecode/GIT_REPOSITORIES/LPP/Users/Tavant/DevCalcul/LPPview
RUN cd LPPview && pip3 install . && cd ..

## Install for documentation
RUN pip install ford && dnf install -y graphviz*
############################
##  Run service script for TeamCity
############################
CMD ["/run-services.sh"]
