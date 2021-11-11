FROM andreadotti/geant4-dev:10.0.p04

ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4NDL.4.4.tar.gz /usr/local/geant4/data/
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4EMLOW.6.35.tar.gz /usr/local/geant4/data
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4PhotonEvaporation.3.0.tar.gz /usr/local/geant4/data
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4RadioactiveDecay.4.0.tar.gz /usr/local/geant4/data
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4SAIDDATA.1.1.tar.gz /usr/local/geant4/data
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4NEUTRONXS.1.4.tar.gz /usr/local/geant4/data
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4PII.1.3.tar.gz /usr/local/geant4/data
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/RealSurface.1.0.tar.gz /usr/local/geant4/data
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4ENSDFSTATE.1.0.tar.gz /usr/local/geant4/data
ADD https://geant4-data.web.cern.ch/geant4-data/datasets/G4ABLA.3.0.tar.gz /usr/local/geant4/data


RUN cd /usr/local/geant4/data && tar xf G4NDL.4.4.tar.gz && rm G4NDL.4.4.tar.gz
RUN cd /usr/local/geant4/data && tar xf G4EMLOW.6.35.tar.gz && rm G4EMLOW.6.35.tar.gz
RUN cd /usr/local/geant4/data && tar xf G4PhotonEvaporation.3.0.tar.gz && rm G4PhotonEvaporation.3.0.tar.gz
RUN cd /usr/local/geant4/data && tar xf G4RadioactiveDecay.4.0.tar.gz && rm G4RadioactiveDecay.4.0.tar.gz
RUN cd /usr/local/geant4/data && tar xf G4SAIDDATA.1.1.tar.gz && rm G4SAIDDATA.1.1.tar.gz
RUN cd /usr/local/geant4/data && tar xf G4NEUTRONXS.1.4.tar.gz && rm G4NEUTRONXS.1.4.tar.gz
RUN cd /usr/local/geant4/data && tar xf G4PII.1.3.tar.gz && rm G4PII.1.3.tar.gz
RUN cd /usr/local/geant4/data && tar xf RealSurface.1.0.tar.gz && rm RealSurface.1.0.tar.gz
RUN cd /usr/local/geant4/data && tar xf G4ENSDFSTATE.1.0.tar.gz && rm G4ENSDFSTATE.1.0.tar.gz
RUN cd /usr/local/geant4/data && tar xf G4ABLA.3.0.tar.gz && rm G4ABLA.3.0.tar.gz


