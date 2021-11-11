FROM silex/emacs@sha256:6e4405cacb36845c297913ff13133ed8c713bceef55d4d5b5b6c4d2e7d928f6f

MAINTAINER Tomoyuki KOYAMA webmaster@koyama.me

RUN git clone https://github.com/kawabata/emacs-trr.git ~/.emacs-trr && \ 
echo "(add-to-list 'load-path \"~/.emacs-trr\")\n(require 'trr)\n;; (setq trr-japanese t)  ;; uncomment this to play with Japanese mode" >> ~/.emacs

# overwrite base-image
WORKDIR /root
ENTRYPOINT ["emacs","-f","trr"]
