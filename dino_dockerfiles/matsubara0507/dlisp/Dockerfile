FROM dlanguage/ldc:latest

WORKDIR /root/dlisp
COPY . /root/dlisp
RUN ldc2 -of/usr/local/bin/plisp *.d ./**/*.d ./**/**/*.d

CMD ["/bin/bash"]
