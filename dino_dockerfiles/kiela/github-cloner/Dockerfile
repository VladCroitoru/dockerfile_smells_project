FROM python:3.6.4-alpine
ENV APPDIR /usr/local/github-cloner
RUN apk update && apk add git \
    && git clone https://github.com/mazen160/GithubCloner.git $APPDIR \
    && pip install -r $APPDIR/requirements.txt \
    && mkdir /output
WORKDIR $APPDIR
ENTRYPOINT ["./githubcloner.py", "--output-path", "/output"]
CMD ["-h"]
