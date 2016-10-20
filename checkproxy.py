#coding=utf-8
 
import urllib2
import urllib
import time
import socket
import os
import random
import time

ip_check_url = 'http://www.mingluji.com/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'
user_agent_list = [\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",\
        "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",\
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",\
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",\
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",\
        "Googlebot/2.1 (+http://www.googlebot.com/bot.html)",\
        "Googlebot/2.1 (+http://www.google.com/bot.html)",\
        "msnbot/1.0 (+http://search.msn.com/msnbot.htm)"
       ]
socket_timeout = 30
ua = random.choice(user_agent_list)
if ua:
    print()

# Check proxy
def check_proxy(protocol, pip): 
  try:
    proxy_handler = urllib2.ProxyHandler({protocol:pip})
    opener = urllib2.build_opener(proxy_handler)
    # opener.addheaders = [('User-agent', user_agent)]
    urllib2.install_opener(opener)

    req = urllib2.Request(ip_check_url)
    time_start = time.time()
    conn = urllib2.urlopen(req)
    # conn = urllib2.urlopen(ip_check_url)
    time_end = time.time()
    detected_pip = conn.read()
    
    proxy_detected = True
 
  except urllib2.HTTPError, e:
    print "ERROR: Code ", e.code
    return False 
  except Exception, detail:
    print "ERROR: ", detail
    return False
 
  return proxy_detected

def main():
  socket.setdefaulttimeout(socket_timeout)

  protocol = "http"
  intput = os.popen('cat /Tools/okips.txt')

  output = open('/Tools/useip.txt','a')

  lines=intput.readlines()
  for line in lines:
      current_proxy=line.strip('\n')
      # current_proxy = "115.231.162.216:3128"

  # output = os.popen('cat /Tools/ip.txt')
  # urlfile=open('/Tools/okip.txt','a')
  # lines=output.readlines()
  # timestr='2016-'
  # for line in lines:
  #     if timestr not in line:
  #           strs=line.split('	')
  #           str1=str(strs).replace('\t',' ')
  #           str0=str1
  #           current_proxy=strs[0]+':'+strs[1]
  #           urlfile .write(str(current_proxy)+'\n')
  #           print(current_proxy)
      proxy_detected = check_proxy(protocol, current_proxy)
      print(proxy_detected)
      if proxy_detected:
          output .write('\'http://'+current_proxy+'\':\''+current_proxy+'\',')

          print (" WORKING: " +current_proxy)

      else:
          print " FAILED: %s " % ( current_proxy, )
  output .close( )


if __name__ == '__main__':
    main()