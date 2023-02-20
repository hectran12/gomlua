import requests, html, time
from requests.structures import CaseInsensitiveDict
import time



def like(id, cookie, id_action):
    try:
        url = "https://mbasic.facebook.com/story.php?story_fbid={1}&id={0}".format(id[0], id[1])

        headers = CaseInsensitiveDict()
        headers["authority"] = "mbasic.facebook.com"
        headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        headers["accept-language"] = "vi,en;q=0.9,en-US;q=0.8"
        headers["cookie"] = cookie
        headers["sec-fetch-dest"] = "document"
        headers["sec-fetch-mode"] = "navigate"
        headers["sec-fetch-site"] = "none"
        headers["sec-fetch-user"] = "?1"
        headers["upgrade-insecure-requests"] = "1"
        headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"


        responsePost = requests.get(url, headers=headers)
        getFullLink = lambda path, first: 'https://mbasic.facebook.com/{0}{1}'.format(first, html.unescape(path.split('"')[0]))
        linkReact = getFullLink(responsePost.text.split('href="/reactions/picker/?is_permalink=1')[1], 'reactions/picker/?is_permalink=1')
        
        # rq to link react
        responseReactPage = requests.get(linkReact, headers=headers)
        getReactLink = responseReactPage.text.split('href="/ufi/reaction/?ft_ent_identifier=')
        linkActionLike = getFullLink(getReactLink[id_action], 'ufi/reaction/?ft_ent_identifier=')
        
        # like
        ActionLike = requests.get(linkActionLike, headers=headers)
    except:
        pass

def loginGomlua (user, pasw):
    url = "https://gomlua.com/user/loginV2?os=web"

    headers = CaseInsensitiveDict()
    headers["authority"] = "gomlua.com"
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "vi,en;q=0.9,en-US;q=0.8"
    headers["origin"] = "https://gomlua.com"
    headers["referer"] = "https://gomlua.com/"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41"

    data = {'email': user, 'password': pasw}


    resp = requests.post(url, headers=headers, data=data).json()

    if resp["status"] == 1:
        return resp 
    else:
        return False

def checkLiveCookieFB (cookie):
    url = "https://mbasic.facebook.com/profile.php"

    headers = CaseInsensitiveDict()
    headers["authority"] = "mbasic.facebook.com"
    headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    headers["accept-language"] = "vi,en;q=0.9,en-US;q=0.8"
    headers["cache-control"] = "max-age=0"
    headers["cookie"] = cookie
    headers["referer"] = "https://mbasic.facebook.com/"
    headers["sec-fetch-dest"] = "document"
    headers["sec-fetch-mode"] = "navigate"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-fetch-user"] = "?1"
    headers["upgrade-insecure-requests"] = "1"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41"


    resp = requests.get(url, headers=headers)

    if "/profile/basic/intro/bio/" in resp.text:
        
        return resp.text.split('<head><title>')[1].split('<')[0]
    else:
        return False
    

def getListJob (token, type):
    url = "https://gomlua.com/cpi/listCampaignFacebook?os=web&type=like_post"

    headers = CaseInsensitiveDict()
    headers["authority"] = "gomlua.com"
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "vi,en;q=0.9,en-US;q=0.8"
    headers["app_token"] = token
    headers["referer"] = "https://gomlua.com/"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-ch-ua"] = '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41"


    resp = requests.get(url, headers=headers).json()

    if resp["status"] == 1:
        job = resp["data"]
        size = job["size"]
        if size == 0 or size < 0:
            return False 
        else:
            # jobOnly = []
            # for x in job["list"]:
            #     if x["react_type"] == type:
            #         jobOnly.append(x)
            # if (len(jobOnly) > 0): return jobOnly
            # else: return False
            return job["list"]
    else:
        return False

def checkLinkLike (token, id):
    url = "https://gomlua.com/cpi/checkLinkLike?os=web&link_id={0}".format(id)

    headers = CaseInsensitiveDict()
    headers["authority"] = "gomlua.com"
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "vi,en;q=0.9,en-US;q=0.8"
    headers["app_token"] = token
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-ch-ua"] = '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41"


    resp = requests.get(url, headers=headers).json()

    if (resp["status"] == 1):
        if (resp["data"]["link_status"] == 1):
            return resp
        else:
            return False 
    else:
        return False

def verifyClaim (token, id):
    url = "https://gomlua.com/cpi/likeSuccess?os=web&link_id={0}&like_old=1".format(id)

    headers = CaseInsensitiveDict()
    headers["authority"] = "gomlua.com"
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "vi,en;q=0.9,en-US;q=0.8"
    headers["app_token"] = token
    headers["referer"] = "https://gomlua.com/"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-ch-ua"] = '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41"


    resp = requests.get(url, headers=headers).json()

    if resp["status"] == 1:
        return resp
    else:
        return False
user_gl = input('User: ')
pass_gl = input("Pass: ")
cookie_fb = input('Cookie fb: ')
infoLogin = loginGomlua(user_gl, pass_gl)
if infoLogin == False:
    print('Tài khoản gom lúa sai!')
    quit()

print('Đăng nhập thành công!')
nameFB = checkLiveCookieFB(cookie_fb)
if nameFB == False:
    print('Cookie fb die')
    quit()

token_gomlua = infoLogin["data"]["app_token"]
buddy = infoLogin["data"]["curent_paddy"]

print('Tài khoản FB:', nameFB)
print('Tiền gomlua:', buddy)

delay = int(input('Delay (khuyên > 10): '))
stt = 0
while True:
    jobLike = getListJob(token_gomlua, "LIKE")
    if jobLike:
        localtime = time.asctime( time.localtime(time.time()) )
        print(localtime, '=>', 'Lấy job thành công', str(len(jobLike)), 'jobs', end='\r')
        for x in jobLike:
            title = x["link_title"]
            link_id = x["link_id"]

            checkLikeClickLink = checkLinkLike(token_gomlua, link_id)

            if checkLikeClickLink == False:
                
                localtime = time.asctime( time.localtime(time.time()) )
                print(localtime, '=>', 'Không xác nhận được để tiến hành làm job', end='\r')
              
            else:
                camp_id = x["campaign_id"].split('_')
                react_type = x["react_type"]
                id_action = 0
                if react_type == "LIKE": id_action = 1 
                elif react_type == "LOVE": id_action = 2
                elif react_type == "HAHA": id_action = 4
                elif react_type == "WOW": id_action = 5
                elif react_type == "CARE": id_action = 3
                elif react_type == "SAD": id_action = 6
                elif react_type == "ANGRY": id_action = 7
                
        
                
                localtime = time.asctime( time.localtime(time.time()) )
                like(id=camp_id, cookie=cookie_fb, id_action=id_action)
                result = verifyClaim(token_gomlua, link_id)
                if result:
                    stt += 1
                    print(localtime, '=>', stt, '=>', react_type, '=>', result['message'], '=>', result['data']['current_paddy'])
            time.sleep(delay)
        time.sleep(delay)
    else:
        localtime = time.asctime( time.localtime(time.time()) )
        print(localtime, '=>', 'Hết job để làm rồi!!!!!!!!!!!!', end='\r')
