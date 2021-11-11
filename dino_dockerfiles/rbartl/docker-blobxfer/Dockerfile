FROM debian

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y libpython3-dev
RUN apt-get install -y libffi-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y python3-pyparsing 

#RUN useradd -m integration


#RUN su integration -c "pip3 install --user --upgrade appdirs"
#RUN su integration -c "pip3 install --user blobxfer"
RUN pip3 install --upgrade appdirs
RUN pip3 install blobxfer
RUN mkdir /transfer

VOLUME /transfer

ENTRYPOINT [ "/usr/local/bin/blobxfer" ]
CMD [ "--help" ]
