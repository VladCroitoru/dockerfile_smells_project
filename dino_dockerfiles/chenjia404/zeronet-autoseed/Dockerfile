FROM nofish/zeronet
RUN apk update && apk add --upgrade tor && apk add sqlite curl
COPY ./autoseed.sh /root/autoseed.sh
COPY ./zeronet.conf /root/zeronet.conf
COPY ./trackers_all.txt /root/data/1Bm8RDrnitgbh7Nbsbo6T9j5VDLWTGaar4/trackers_all.txt
RUN chmod a+x /root/autoseed.sh
RUN echo '*  *  *  *  *    /root/autoseed.sh' > /etc/crontabs/root
CMD  (! ${ENABLE_TOR} || tor&) && crond && python zeronet.py --ui_ip 0.0.0.0 --fileserver_port 20184
