FROM base/archlinux:latest

MAINTAINER fdiblen

ENV container docker
ENV LC_ALL en_US.UTF-8

USER root

# ADD NORMAL USER
#===========================================
RUN useradd -ms /bin/zsh -G users,wheel archsci \
    && echo "archsci:archsci" | chpasswd


# ADD SCRIPTS
#===========================================
RUN mkdir -p /home/archsci/temp
RUN mkdir -p /home/archsci/temp/scripts
RUN mkdir -p /home/archsci/temp/services

COPY scripts/* /home/archsci/temp/scripts/
RUN chmod +x /home/archsci/temp/scripts/*.sh

COPY confs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY services/* /home/archsci/temp/services

COPY confs/zshrc.template /home/archsci/.zshrc
COPY confs/antigen.template /home/archsci/.antigen.archsci
COPY confs/pacman.conf /home/archsci/temp


# INSTALL AUR HELPER AND PACKAGES
#===========================================
RUN /home/archsci/temp/scripts/install_packages.sh


# SET ENVIRONMENT, USER and SUDO
#===========================================
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "en_US ISO-8859-1" >> /etc/locale.gen \
    && locale-gen

RUN echo "archsci    ALL=(ALL)    NOPASSWD:ALL" >> /etc/sudoers.d/archsci

WORKDIR /home/archsci
RUN chown archsci:archsci -R /home/archsci

RUN echo "export SHELL=/usr/bin/zsh" >> /etc/profile



# NORMAL USER
#===========================================
USER archsci
ENV HOME /home/archsci
ENV DISPLAY :0
ENV EDITOR vim
ENV TERM xterm-256color
ENV USER archsci
ENV SHELL /usr/bin/zsh


# AUR PACKAGES
#===========================================
WORKDIR /home/archsci
RUN /home/archsci/temp/scripts/install_packages_aur.sh


# SET the shell
#===========================================
RUN /home/archsci/temp/scripts/set_shell.sh


# SETUP services
#===========================================
RUN /home/archsci/temp/scripts/setup_services.sh


# CLEAN UP
#===========================================
RUN /home/archsci/temp/scripts/clean.sh
RUN sudo rm -rf /home/archsci/temp


EXPOSE 22
CMD ["sudo","/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
#CMD ["/bin/zsh"]
