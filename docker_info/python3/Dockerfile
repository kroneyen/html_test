FROM centos:latest

### setting  OS LANG && python folder 
RUN export LANG="en_US.UTF-8" 
RUN mkdir /root/python_dir

### adding google-chrome.repo mapping 
ADD conf/google-chrome.repo /etc/yum.repos.d/ 
ADD conf/contab_default.sh /root/python_dir/
ADD conf/random_range.sh /root/python_dir/
ADD conf/req.txt /root/python_dir/

### install OS && chrome  package
RUN yum update -y 
RUN yum install -y yum-utils \
    wget \
    Xvfb \
    zip \
    unzip \
    crontabs \
    google-chrome-stable 

RUN yum groupinstall -y 'Development Tools' 
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm 
#RUN yum update 
    

### install  python 3X & pip 
RUN yum install -y python36u \
    python36u-pip \
    python36u-libs 


### update default 2.7 pip to pip 18.0 
#RUN pip3.6 install --upgrade pip  ## from 9.1 to 10.1   
#RUN pip3.6 install --upgrade pip ## from 10.1 to 18.0
    

### install python module 
#RUN pip3.6 install -U pip \
#    selenium \
#    pyvirtualdisplay \
#    requests \
#    beautifulsoup4 \
#    setuptools 
RUN pip3.6 install -r /root/python_dir/req.txt

### install chromedriver  && setting PATH
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip 
RUN unzip chromedriver_linux64.zip -d /usr/bin 
RUN cp /usr/bin/chromedriver /usr/local/bin/  ## dev evn static path for crontab


### adding --no-sandbox avoid chrome : unknown error: DevToolsActivePort file doesn't exist    
RUN sed -i 's/exec -a "$0" "$HERE\/chrome" "$@"'/'exec -a "$0" "$HERE\/chrome" "$@" --no-sandbox/g' \
     /usr/bin/google-chrome 

### execute python contable 
RUN /root/python_dir/contab_default.sh
#CMD ["/bin/sh","/root/python_dir/contab_default.sh"]
