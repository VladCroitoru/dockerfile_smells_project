FROM library/openjdk:13-slim
COPY target/cli-0.0.1-SNAPSHOT.jar /root/cloudflare-cli
CMD java -Dcloudflare.email=${EMAIL} -Dcloudflare.apikey=${KEY} -Dcloudflare.accountId=${ID} -jar /root/cloudflare-cli