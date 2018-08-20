FROM centos:latest

### setting  OS LANG && python folder 

ENV LANG en_US.UTF-8 
ENV work_conf  /root/python_conf/
RUN mkdir -p $work_conf


### create work folder 
WORKDIR $work_conf

### adding google-chrome.repo mapping 
COPY conf/google-chrome.repo /etc/yum.repos.d/ 
COPY conf/crontab_default.sh conf/random_range.sh conf/req.txt $work_conf
#COPY conf/random_range.sh $work_conf
#COPY conf/req.txt $work_conf
#COPY conf/random_range.sh /root/python_dir/
#COPY conf/req.txt /root/python_dir/

### install OS && chrome  package

RUN yum update -y 
RUN yum install -y yum-utils \
    wget \
    Xvfb \
    zip \
    unzip \
    crontabs \
    google-chrome-stable \
    https://centos7.iuscommunity.org/ius-release.rpm


#RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm 

### install  python 3X & pip 
RUN yum install -y python36u \
    python36u-pip \
    python36u-libs \
    python36u-setuptool

### install python module 

RUN pip3.6 install -r req.txt

### install chromedriver  && setting PATH ChromeDriver 2.41
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip 
RUN unzip chromedriver_linux64.zip 
RUN cp chromedriver /usr/bin/; cp chromedriver /usr/local/bin 


### adding --no-sandbox avoid chrome : unknown error: DevToolsActivePort file doesn't exist    
RUN sed -i 's/exec -a "$0" "$HERE\/chrome" "$@"'/'exec -a "$0" "$HERE\/chrome" "$@" --no-sandbox/g' /usr/bin/google-chrome 

### execute python contable 
RUN /bin/sh crontab_default.sh
