FROM silex/emacs:27.1

RUN apt update
RUN apt install -y git
RUN rm -rf /root/.emacs.d
RUN cd /root && git clone https://github.com/LaurenceWarne/emacs.d .emacs.d

CMD ["emacs"]