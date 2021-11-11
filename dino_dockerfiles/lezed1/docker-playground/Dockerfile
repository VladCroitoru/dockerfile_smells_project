FROM phusion/baseimage:0.9.22
CMD ["/sbin/my_init"]
RUN rm -f /etc/service/sshd/down

RUN mkdir /dependencies && chmod -R 755 /dependencies

COPY install/foundation-install.sh /dependencies/
RUN bash /dependencies/foundation-install.sh

COPY install/setup-user.sh /dependencies/
RUN bash /dependencies/setup-user.sh

COPY install/ocaml-install.sh /dependencies/
RUN bash /dependencies/ocaml-install.sh
COPY install/ocaml-user-install.sh /dependecies/
RUN setuser software /dependecies/ocaml-user-install.sh

COPY install/spacemacs-install.sh /dependencies/
RUN bash /dependencies/spacemacs-install.sh
COPY install/dot-spacemacs /home/software/.spacemacs
RUN setuser software emacs --batch -u software --kill

COPY install/node-install.sh /dependencies/
RUN bash /dependencies/node-install.sh

COPY install/apt-install.sh /dependencies/
RUN bash /dependencies/apt-install.sh

COPY install/pip-install.sh /dependencies/
RUN bash /dependencies/pip-install.sh

COPY install/misc-install.sh /dependencies/
RUN bash /dependencies/misc-install.sh

COPY install/extra-install.sh /dependencies/
RUN bash /dependencies/extra-install.sh

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache /dependencies


# USER software
# WORKDIR /home/software/cuauv/software
# CMD ip a && sudo service ssh start && echo "CUAUV Docker container running! C-c to stop the container" && cat
