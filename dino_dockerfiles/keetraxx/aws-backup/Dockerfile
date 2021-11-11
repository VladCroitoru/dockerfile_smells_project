FROM python:3-alpine

RUN apk --no-cache add bash bash-completion groff

RUN pip install awscli
RUN mkdir -p /etc/bash_completion.d
RUN ln -s /usr/local/bin/aws_bash_completer /etc/bash_completion.d/aws_bash_completer

RUN echo '[[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] && . /usr/share/bash-completion/bash_completion' >> /root/.bashrc

ADD s3-backup.sh /usr/local/bin/s3-backup.sh


CMD s3-backup.sh
