FROM sgeisler/java8-maven

RUN \ 
  apt-get install -y openjfx

# clone and install bitcoinj
WORKDIR /local/git
RUN git clone -b FixBloomFilters https://github.com/bitsquare/bitcoinj.git
WORKDIR /local/git/bitcoinj
RUN mvn clean install -DskipTests -Dmaven.javadoc.skip=true

RUN \
  wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip && \
  unzip jce_policy-8.zip && \
  cp UnlimitedJCEPolicyJDK8/US_export_policy.jar /usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib/security/US_export_policy.jar && \
  cp UnlimitedJCEPolicyJDK8/local_policy.jar /usr/lib/jvm/java-1.8.0-openjdk-amd64/jre/lib/security/local_policy.jar && \
  rm -r UnlimitedJCEPolicyJDK8 && \
  rm jce_policy-8.zip

WORKDIR /local/git

