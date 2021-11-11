FROM apluslms/grade-python:3.7-3.5-3.4

ARG VERSION=2.5.5
ARG NAME=MiniZincIDE-$VERSION-bundle-linux-x86_64

RUN cd /tmp \
    && curl -LOSs https://github.com/MiniZinc/MiniZincIDE/releases/download/$VERSION/$NAME.tgz \
    && tar -xzf $NAME.tgz \
    && (cd $NAME \
     && cp bin/minizinc* bin/fzn-* bin/findMUS bin/mzn2doc /usr/local/bin \
     && cp -r share/minizinc /usr/local/share/ \
     && cp -r lib /usr/local/lib/minizinc \
    ) \
    && rm -rf $NAME.tgz $NAME

ENV MZN_STDLIB_DIR=/usr/local/share/minizinc/
