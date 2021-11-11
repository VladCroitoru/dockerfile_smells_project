FROM perl:5
COPY . /http/bombard
WORKDIR /http/bombard
RUN cpanm --installdeps .
RUN chmod +x http-bombardment
ENTRYPOINT ["./http-bombardment"]
