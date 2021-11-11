FROM centos:centos7
  MAINTAINER Jeremy Marshall
  RUN yum -y install ksh java-1.7.0-openjdk git cpanm gcc perl perl-App-cpanminus perl-Config-Tiny install perl-File-Which  perl-XML-Simple perl-Archive-Zip perl-JSON perl-Test-Warn perl-HTTP-Message &&  yum clean all &&  cpanm Selenium::Remote::Driver && rm -fr root/.cpan/work

  ADD swarm-client-2.0-jar-with-dependencies.jar swarm-client-2.0-jar-with-dependencies.jar

  ENTRYPOINT ["java", "-jar", "swarm-client-2.0-jar-with-dependencies.jar", "-labels", "perl", "-labels", "selenium"  ]


