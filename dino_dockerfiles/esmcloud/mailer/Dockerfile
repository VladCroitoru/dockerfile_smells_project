FROM busybox
COPY . /mailer
WORKDIR /mailer

RUN adduser -DHs /bin/bash test_adduser

RUN chown test_adduser mailer.sh
RUN chmod a+x mailer.sh
EXPOSE 33333

USER test_adduser
CMD ["/mailer/mailer.sh"]
