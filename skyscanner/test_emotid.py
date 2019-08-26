# -*- coding: utf-8 -*-


import random
#import send_mail
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import re


thtml ="""
<form method="post" id="signform" action="plugin.php?id=awa_signin:sign" onsubmit="ajaxpost(this.id, 'floatlayout_signin','','onerror');return false;">
<input type="hidden" name="formhash" value="32fff9e4">
<input type="hidden" name="signsubmit" value="yes">
<input type="hidden" name="handlekey" value="signin">
<input type="hidden" name="emotid" id="emotid">
<input type="hidden" name="referer" value="https://awabest.com/./">
<div class="layer_dcsignin">
<div class="dcsignin_title"></div>
<ul class="dcsignin_list">
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==11?this.className:''" onclick="check(this, 11)" class="">
  <div class="dcsignin2">
     <img width="32" height="32" id="emot_11" src="source/plugin/awa_signin/images/emot/01.png" title="" alt="開心">開心
  </div>
</li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==12?this.className:''" onclick="check(this, 12)"><div class="dcsignin2"><img width="32" height="32" id="emot_12" src="source/plugin/awa_signin/images/emot/02.png" title="" alt="想睡">想睡</div></li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==13?this.className:''" onclick="check(this, 13)"><div class="dcsignin2"><img width="32" height="32" id="emot_13" src="source/plugin/awa_signin/images/emot/03.png" title="" alt="戀愛">戀愛</div></li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==21?this.className:''" onclick="check(this, 21)" class=""><div class="dcsignin2"><img width="32" height="32" id="emot_21" src="source/plugin/awa_signin/images/emot/04.png" title="" alt="憤怒">憤怒</div></li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==22?this.className:''" onclick="check(this, 22)" class=""><div class="dcsignin2"><img width="32" height="32" id="emot_22" src="source/plugin/awa_signin/images/emot/05.png" title="" alt="驚恐">驚恐</div></li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==23?this.className:''" onclick="check(this, 23)"><div class="dcsignin2"><img width="32" height="32" id="emot_23" src="source/plugin/awa_signin/images/emot/06.png" title="" alt="難過">難過</div></li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==24?this.className:''" onclick="check(this, 24)"><div class="dcsignin2"><img width="32" height="32" id="emot_24" src="source/plugin/awa_signin/images/emot/07.png" title="" alt="迷茫">迷茫</div></li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==25?this.className:''" onclick="check(this, 25)"><div class="dcsignin2"><img width="32" height="32" id="emot_25" src="source/plugin/awa_signin/images/emot/08.png" title="" alt="鬱悶">鬱悶</div></li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==26?this.className:''" onclick="check(this, 26)"><div class="dcsignin2"><img width="32" height="32" id="emot_26" src="source/plugin/awa_signin/images/emot/09.png" title="" alt="發呆">發呆</div></li>
<li onmouseover="this.className='current'" onmouseout="this.className=$('emotid').value==20?this.className:''" onclick="check(this, 20)"><div class="dcsignin2"><img width="32" height="32" id="emot_20" src="source/plugin/awa_signin/images/emot/10.png" title="" alt="秘密">秘密</div></li>
</ul>
<div class="dcsignin_send">
 		
 	</div>
</div>
<p class="o pns">
<button type="submit" name="signpn" value="true" class="pn pnc"><strong>確定</strong></button>
</p>
</form>
"""



def get_emot_id(thtml):
    ###find(name,attrs,recursive,text,**wargs)
    emotid_list = []
    soup = BeautifulSoup(thtml, "html.parser")
    #print(soup)
    #sign_form = soup.find('div', attrs={'class':re.compile('layer_dcsignin')})  ## 找出隱藏的from : signform
    dcsignin2_list = soup.find_all('div', attrs={'class': re.compile('dcsignin2')})  ## 找出隱藏的from : signform
    for dcsignin2 in dcsignin2_list :
        img_list = dcsignin2.find('img')
        emotid_list.append(img_list.get('id'))

    ran_rows = random.randrange(0, len(emotid_list), 1)  ## get random
    return emotid_list[ran_rows]
    #print(emotid_list)
        #dcsignin_list = sign_form.find_all('ul', attrs={'class':re.compile('dcsignin_list')})  ## 找出隱藏的 dcsignin_list
    #print(dcsignin_list)
    #dcsignin_list = soup.find('ul')  ## 找出隱藏的 dcsignin_list

    #li_list = dcsignin_list.find_all('div', attrs={'class':re.compile('dcsignin2')})  ## 找出隱藏的 每個圖案
    #print(li_list)
    """
    for emotid in li_list.find_all('img', attrs={'fwin': re.compile('sign')}):
        emotid_list.append(emotid.get('id'))  ##紀錄目前 emotid

    ran_rows = random.randrange(0, len(emotid_list), 1)  ## get random
    print(emotid_list[ran_rows])
    #non_rep_link_list = random.sample(emotid_list, k=ran_rows)
    return emotid_list[ran_rows]
    """

emotid_list =get_emot_id(thtml)
print(emotid_list)