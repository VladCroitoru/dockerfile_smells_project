# Customized Docked Fedora 31 for running Fluka
# ========================================================
# dr.vittorio.boccone@ieee.org
# vittorio.boccone@dectris.com
# andrea.fontana@pv.infn.it
# docker run -i --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -v $(pwd):/local_path -t my_fedora_for_fluka bash
ARG fedora_for_fluka_repo

FROM $fedora_for_fluka_repo
ARG fluka_package
RUN dnf install -y gfortran gcc-gfortran-9.2.1

# Copy fluka to local folder
COPY $fluka_package /tmp

RUN dnf install -y /tmp/$fluka_package
# RUN mkdir -p /opt/fluka
# RUN tar -zxvf /tmp/*.tar.gz -C /opt/fluka
# ENV FLUFOR=gfortran
# ENV FLUPRO=/opt/fluka
# RUN cd /opt/fluka; make

# RUN chown -R fluka:fluka /opt/fluka
# RUN chmod -R g+rw /opt/fluka
# RUN chmod g+x /opt/fluka/flutil/fff
# RUN chmod g+x /opt/fluka/flutil/rfluka
# RUN chmod g+x /opt/fluka/flutil/ldpmqmd
# RUN chmod g+x /opt/fluka/flutil/lfluka
# RUN chmod g+x /opt/fluka/flutil/lflukac
# RUN chmod g+x /opt/fluka/flutil/pawlevphi.kumac

# Remove tmp file
RUN rm -rf /tmp/*.gz

RUN dnf install -y net-tools sudo
# RUN dnf -y update && dnf -y install openssh-server passwd && dnf clean all

# EXPOSE 22
# RUN /usr/bin/ssh-keygen -A

# CMD ["/usr/sbin/sshd", "-D"]

