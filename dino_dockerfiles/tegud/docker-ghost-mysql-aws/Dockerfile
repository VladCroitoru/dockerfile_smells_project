FROM ghost:3.32.2

RUN npm install ghost-storage-adapter-s3 \
	&& mkdir -p /var/lib/ghost/versions/$(ls /var/lib/ghost/versions/)/core/server/adapters/storage/s3 \
	&& cp -r ./node_modules/ghost-storage-adapter-s3/* /var/lib/ghost/versions/$(ls /var/lib/ghost/versions/)/core/server/adapters/storage/s3 \
	&& cp -r ./node_modules/aws-sdk/* /var/lib/ghost/versions/$(ls /var/lib/ghost/versions/)/node_modules/aws-sdk/
