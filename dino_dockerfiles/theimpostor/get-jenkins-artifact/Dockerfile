FROM perl:5

RUN cpanm REST::Client JSON Digest::MD5::File

COPY get-artifact.pl /usr/bin

ENTRYPOINT [ "/usr/bin/get-artifact.pl" ]
