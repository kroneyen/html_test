FROM centos:latest


## OS install soft
RUN yum update -y && yum install -y epel-release \
    https://centos7.iuscommunity.org/ius-release.rpm \
    python36u \
    python36u-pip \
    python36u-devel \
    Xvfb \
    Wget \
    zip \
    unzip \
    python36u-libs \
    crontabs\
    #&& cd /usr/bin/ \
    #&& ln -s /usr/bin/python3.6 python3\

     
## python install model
RUN /usr/bin/python3.6 -m pip install selenium \
    pyvirtualdisplay \
    requests \
    logging \
    random \
    datetime \
    time \
    BeautifulSoup \
    smtplib \
    re \
    calendar\ 
    #&&  pip3 -v

RUN mkdir python 
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d ~/python

CMD ["python3"]   
