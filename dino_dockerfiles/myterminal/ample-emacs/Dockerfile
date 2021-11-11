FROM myterminal/linux-dev

MAINTAINER Mohammed Ismail Ansari <team.terminal@gmail.com>

LABEL description "A docker image featuring ample-emacs"
LABEL version "0.9.1"

RUN useradd dev
ENV HOME /home/dev

WORKDIR /home/dev
RUN git clone https://github.com/myTerminal/ample-emacs.git
RUN mv ample-emacs/.emacs.d . && rm ample-emacs -rf && rm .emacs

CMD ["/bin/bash"]
