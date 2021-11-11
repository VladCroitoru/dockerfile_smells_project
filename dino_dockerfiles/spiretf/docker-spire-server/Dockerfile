from spiretf/docker-comp-server
maintainer Robin Appelman <robin@icewind.nl>

USER root
ADD ./server.cfg $SERVER/tf2/tf/cfg/server.cfg
RUN chown tf2:tf2 $SERVER/tf2/tf/cfg/server.cfg
USER $USER

ADD ./tf.sh $SERVER/tf.sh

ENTRYPOINT ["./tf.sh"]
CMD ["+sv_pure", "1", "+mapcycle", "mapcycle_quickplay_payload.txt", "+maxplayers", "24"]
