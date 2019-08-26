

import redis

pool = redis.ConnectionPool(host='10.20.16.99', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
#r.flushall()
#r.delete('myusername_list')
#print(r.keys('p2p*'))
#print(r.lrange('p2p_myusername_list',0,-1))
#print(r.lrange('p2p_mypassword_list',0,-1))
#print(r.lrange('p2p_uid_list',0,-1))

import redis

# import StrictRedis
pool = redis.ConnectionPool(host='10.20.16.99', port=6379, decode_responses=True)
r = redis.StrictRedis(connection_pool=pool)


"""
def get_redis_tid(my_history):

    return my_history , r.lrange(my_history,0,-1)

my_history_list = r.keys('myreply_history*')

for my_history in   my_history_list :
   logg , my_tid_lists =get_redis_tid(my_history)
   print(logg)
   for i in my_tid_lists :
     print(i)
   print('==================')
"""
for i in  r.keys('*') :
    print(i)


#logg ,my_tid_lists =get_redis_tid('myreply_history_fat1209')


#print(logg)
#print(my_tid_lists)






"""
r.flushall()

###p2p 
r.rpush("p2p_myusername_list", 'fat1209','k20180317','j20180702')
r.rpush("p2p_mypassword_list", '05161209','20180317k','20180702j')
r.rpush("p2p_uid_list",'750995','2045238','2053337')


### apk 
r.rpush("apk_myusername_list", 'fat1209')
r.rpush("apk_mypassword_list", 'R9DMPqn2jS')
r.rpush("apk_uid_list",'2898458')


### awa

r.rpush("awa_myusername_list", 'pekrone')
r.rpush("awa_mypassword_list", 'E0orRTpVQBl5cI5')
r.rpush("awa_uid_list",'57990')

### no_ip

r.rpush("no_ip_myusername_list", 'krone.huang@gmail.com')
r.rpush("no_ip_mypassword_list", '1d7shInJ00SbfCGN4FM0')
r.rpush("no_ip_domain_list",'kronehuang.ddns.net','pekrone.ddns.net','pekrone.myftp.org')

### mail

r.hmset("mail",{'m_from':'ingeniousinc2016@gmail.com','m_to':'krone.huang@gmail.com','m_pwd':'Qwer2016'})


#print(r.smembers('p2p_myusername_list'))
#print(r.scard('p2p_myusername_list'))
#print(r.sismember('p2p_myusername_list','123456'))
#print(r.lrange('p2p_myusername_list',0,-1))






#print(r.hmget('8_2','bank_card_seq','total_count','location'))

#print(r.hgetall('8_2'))
#print((r.lrange('myusername_list',0,3)))

#r.hmset("p2p",{'myusername_list':'fat1209,k20180317,j20180702'})

.delete('myusername_list','mypassword_list','uid_list')

r.rpush("myusername_list", 'fat1209','k20180317','j20180702')
r.rpush("mypassword_list", '05161209','20180317k','20180702j')
r.rpush("uid_list",'750995','2045238','2053337')

r.hmset("mail",{'m_from':'ingeniousinc2016@gmail.com','m_to':'krone.huang@gmail.com','m_pwd':'Qwer2016'})
r.hmset("p2p",{'myusername_list':'fat1209','k20180317','j20180702'})

#print(r.lrange('myusername_list',0,r.llen('myusername_list')))
#print(r.lrange('mypassword_list',0,r.llen('mypassword_list')))
#print(r.lrange('uid_list',0,r.llen('uid_list')))

for i in reversed((r.lrange('myusername_list',0,-1))) :
   print(i)

for j in reversed((r.lrange('mypassword_list',0,-1))) :
   print(j)
#print(r.lrange('myusername_list',0,-1),r.lrange('mypassword_list',0,-1),r.lrange('uid_list',0,-1))
#print(r.lrange('myusername_list',0,0))
#print(r.lrange('mypassword_list',0,-1))
#print(r.lrange('uid_list',0,-1))
#print(r.hkeys('mail'))
#print(r.hvals('mail'))
#print(r.hget('mail','m_from'))
#print(r.hget('mail','m_to'))
#print(r.hget('mail','m_pwd'))
#print(r.hget('p2p','myusername_list'))
#r.flushall()

#r.delete('myusername_list','mypassword_list','uid_list')
"""