FROM scratch
MAINTAINER professorkaos64

# Credit: https://github.com/binhex/arch-scratch

# additional files
##################

# add bootstrap files
ADD bootstrap/shim/shim /.shim
ADD bootstrap/cert/cert /.cert
ADD bootstrap/ducktape/ducktape /.ducktape

# install app
#############

# run shim to set execute permissions for ducktape
RUN ["/.shim", ""]

# run ducktape to download and extract root tarball
RUN ["/.ducktape", "https://github.com/ProfessorKaos64/arch-scratch/releases/download/20170518-i686/root.tar.bz2"]

# remove bootstrap files
RUN /usr/bin/rm -f /.shim /.cert /.ducktape /.dockerenv /.dockerinit

# set entry point as /bin/bash
CMD ["/bin/bash"]
ENTRYPOINT ["linux32", "--"]
