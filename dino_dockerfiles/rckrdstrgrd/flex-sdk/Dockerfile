FROM rckrdstrgrd/flex-sdk:base
RUN mkdir /src
RUN mkdir /output
VOLUME /output
VOLUME /src
COPY ./build.sh /build.sh
COPY ./run.sh /run.sh
RUN chmod +x build.sh && chmod +x run.sh
CMD [ "/run.sh"]