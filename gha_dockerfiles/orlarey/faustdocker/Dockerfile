
########################################################################
########################################################################
#
#       		  Faust in a docker container
#                 (GRAME / Y. Orlarey)
#
########################################################################
########################################################################


FROM alpine:latest 

RUN apk update 
RUN apk add --no-cache gcc musl-dev cmake g++ make git pkgconfig libexecinfo libexecinfo-dev

#COPY faust /faust
RUN git clone --depth 1 https://github.com/grame-cncm/faust.git
RUN make -C /faust/build cmake CMAKEOPT='-DFAUST_DEFINITIONS="-DALPINE"'
RUN make -C /faust/build 
RUN make -C /faust/build install

FROM alpine:latest

RUN apk add --no-cache libstdc++

# We copy all but faust2xxx scripts (they can't be used)
COPY --from=0 /usr/local/bin/faust /usr/local/bin 
COPY --from=0 /usr/local/bin/faustoptflags /usr/local/bin 
COPY --from=0 /usr/local/bin/usage.sh /usr/local/bin 
COPY --from=0 /usr/local/bin/filename2ident /usr/local/bin/
COPY --from=0 /usr/local/bin/sound2reader /usr/local/bin/
COPY --from=0 /usr/local/share/faust/ /usr/local/share/faust/
COPY --from=0 /usr/local/include/faust/ /usr/local/include/faust/

WORKDIR /tmp

ENTRYPOINT [ "/usr/local/bin/faust" ]
CMD [ "-v" ]
