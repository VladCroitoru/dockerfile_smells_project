FROM tutum/mongodb:3.2
MAINTAINER Fredrik Teschke <f@ftes.de>

# run as replica set instead of master/slave, and remove deprecated --rest and --httpinterface
RUN sed -i 's/--httpinterface --rest --master/--replSet rs0/' run.sh

# before changing the password, the replication set has to be initialized
RUN sed -i '/\$cmd \&/a \
./init-replica-set.sh' run.sh

ADD init-replica-set.sh ./init-replica-set.sh

# create oplogger user
RUN echo 'echo "Creating user oplogger:password with read permissions on database local"' >> set_mongodb_password.sh
RUN echo 'mongo admin -u $USER -p $PASS << EOF' >> set_mongodb_password.sh
RUN echo 'db.createUser({user: "oplogger", pwd: "password", roles: [{role: "read", db: "local"}]})' >> set_mongodb_password.sh
RUN echo 'EOF' >> set_mongodb_password.sh
