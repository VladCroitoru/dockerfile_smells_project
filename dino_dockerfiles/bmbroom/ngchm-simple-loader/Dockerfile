# Create a local instance of the NGCHM Simple Loader for connecting to a local
# NGCHM server using the 'Simple CHM Loader' protocol.

# To run:
# - Run to create a data container:
#   docker run --name loader-data bmbroom/ngchm-simple-loader date
# - Run using volumes from both the chmdata and loader-data volumes:
#   docker run --name loader-software --volumes-from chmdata --volumes-from loader-data bmbroom/ngchm-simple-loader
# Creating separate loader-data and loader-software containers allows the loader-software container
# to be stopped, (upgraded,) and restarted independently of the users of loader-data.
#
# - Configure users of the container to import the volumes from the loader-data container.

FROM debian:testing

MAINTAINER Bradley Broom <bmbroom@mdanderson.org>

RUN apt-get update && apt-get -y install inotify-tools && apt-get -y clean

# These must match the imported chmdata directory.
ENV CHMDATA /chmData
ENV CHMUSER chmuser
ENV CHMGROUP chmuser
ENV CHMUID 999
ENV CHMGID 999
RUN groupadd -g $CHMGID -o $CHMGROUP && useradd -g $CHMGID -u $CHMUID -o $CHMUSER

ENV SIMPLEDIR /ngchm.local
ADD ngchm.local $SIMPLEDIR
RUN chown -R $CHMUSER:$CHMGROUP $SIMPLEDIR && \
    bash -c "chmod 3777 $SIMPLEDIR/{ADD,ADD-FILE,REMOVE,REMOVE-FILE,STAGE}"
VOLUME $SIMPLEDIR

ADD scl-driver.sh /

USER $CHMUSER

CMD ["sh", "-c", "exec /scl-driver.sh $CHMDATA localhost:$SIMPLEDIR"]

