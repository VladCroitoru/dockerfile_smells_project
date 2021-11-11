FROM troglodyne/base:latest

ARG port=5000
LABEL description="tCMS: a Perl CMS by Troglodyne LLC"

ADD . /home/tcms
RUN chown -R tcms /home/tcms

USER tcms

RUN make install
ENTRYPOINT ["/usr/bin/starman","www/server.psgi"]
CMD ['-p',$port]
