
FROM mcr.microsoft.com/dotnet/framework/sdk

# Download OpenJDK
ENV JAVA_URL https://download.java.net/java/GA/jdk13.0.2/d4173c853231432d94f001e99d882ca7/8/GPL/openjdk-13.0.2_windows-x64_bin.zip   
RUN $client = New-Object System.Net.WebClient; \
    $client.DownloadFile("$env:JAVA_URL", \"\openjdk-13.0.2_windows-x64_bin.zip\")

# Install Java
RUN Expand-Archive openjdk-13.0.2_windows-x64_bin.zip
RUN SetX /M PATH "\"\openjdk-13.0.2_windows-x64_bin\jdk-13.0.2\bin;$env:PATH\""
RUN SetX /M JAVA_HOME "\"\openjdk-13.0.2_windows-x64_bin\jdk-13.0.2\""

ENV SONARSCANNER_URL https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.7.1.2311/sonar-scanner-msbuild-4.7.1.2311-net46.zip
RUN $client = New-Object System.Net.WebClient; \
    $client.DownloadFile("$env:SONARSCANNER_URL", \"\sonar-scanner-msbuild-4.7.1.2311-net46.zip\")

RUN Expand-Archive sonar-scanner-msbuild-4.7.1.2311-net46.zip
RUN SetX /M PATH "\"\sonar-scanner-msbuild-4.7.1.2311-net46;$env:PATH\""

# Copy SonarScanner settings to container
COPY SonarQube.Analysis.xml /sonar-scanner-msbuild-4.7.1.2311-net46/SonarQube.Analysis.xml