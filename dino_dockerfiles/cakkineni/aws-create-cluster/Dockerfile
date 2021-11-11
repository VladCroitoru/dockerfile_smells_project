FROM progrium/busybox
RUN mkdir -p /etc/ssl && mkdir -p /etc/ssl/certs
ADD certs /etc/ssl/certs/
ADD create_cluster create_cluster
ADD cloud-config-agent.yaml cloud-config-agent.yaml
ADD cloud-config-init.yaml cloud-config-init.yaml
ADD aws_ami.json aws_ami.json
RUN chmod +x create_cluster
CMD "./create_cluster"
#docker run -e ETCD_API=172.17.42.1:4001 -e AWS_ACCESS_KEY_ID=xxxxxxxx   -e "AWS_SECRET_ACCESS_KEY=xxxxxxx"  -e REGION=ap-northeast-1 -e NODE_COUNT=1 -e VM_SIZE=t1.micro cakkineni/aws-create-cluster:latest

