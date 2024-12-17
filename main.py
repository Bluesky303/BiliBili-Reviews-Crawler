import search
import reviews
import wordsCount
import os
import pandas as pd

# 找一下位置，加点目录
CURRENT_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_PATH)
CURRENT_DIR = CURRENT_DIR.replace("\\","/")
RESULTS_DIR = CURRENT_DIR + "/results"

time_list = [(1451577600,1467302400),(1467302400,1483200000)]
keyword_list = ['川普','特朗普']
cookies = "header_theme_version=CLOSE; buvid4=4DBBBD15-51B9-D1B2-A929-6CFAC1DEC55A00581-023070213-7dgm9TdQFS7%2F4RdSwimvtA%3D%3D; DedeUserID=302619350; DedeUserID__ckMd5=1592de3c292853ab; buvid_fp_plain=undefined; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; buvid3=136B6CAA-CB5B-D16E-6F69-EB22F403CFD656582infoc; b_nut=1719817657; _uuid=818DCC86-8F26-A114-C4A4-5D43211C3AD795363infoc; hit-dyn-v2=1; rpdid=|(um~Ru|m)kl0J'u~kk)J))Ym; LIVE_BUVID=AUTO7017263941872514; fingerprint=2e7a877861ac60165ae2a0eda98be2ba; buvid_fp=2e7a877861ac60165ae2a0eda98be2ba; PVID=2; home_feed_column=5; browser_resolution=1699-941; bp_t_offset_302619350=1010467231923961856; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; CURRENT_FNVAL=4048; b_lsid=10232756A_193D38614A0; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQ2Nzk3OTksImlhdCI6MTczNDQyMDUzOSwicGx0IjotMX0.pNCrA8AFWTFpagPQK93BQYc20OQCni1A94lZf4hxhiM; bili_ticket_expires=1734679739; SESSDATA=79c52da5%2C1749972599%2Ce4386%2Ac2CjBhezSALHe0VnBHmpvgeYXaQJdZBk8r2htKlgd_TbJ-D-JsRbIu4IWQ-ymNWdTgPX8SVklNUjlCbEI4dEdGTlBkdjVwWkhzYmdBU3JLZGR4S21TbmxpSWd2QlZfNURJUDM1WVFvdFlkV0hSZzUxcG5KS0JwVFFUNnQ5LU9uM3g1LTkzbG1EdGl3IIEC; bili_jct=7f9ec53d99dd3f0d061e2dca051202ec; sid=gubu1jh4"

if __name__ == '__main__':
    '''执行所有操作'''
    search.time_list_search(keyword_list=keyword_list, time_list=time_list)
    data = pd.read_excel(RESULTS_DIR + f'/excel/{keyword_list[0]}.xlsx', sheet_name=None)
    names = data.keys()
    for name in names:
        if not name == 'all':
            filename=f'{keyword_list[0]}-{name}'
            bvlist = data[name].iloc[:, 2]
            comments = []
            for num in range(len(bvlist)):
                print(f'{name}-{num+1}/{len(bvlist)}')
                comments += reviews.fetch_comments(bvlist[num], cookies=cookies, max_pages=2)
            contents = []
            for comment in comments:
                contents.append(reviews.purify(comment['content']))
            reviews.write_txt(contents, filename=filename+'.txt')
            wordsCount.save_words_to_all(file_name=filename)