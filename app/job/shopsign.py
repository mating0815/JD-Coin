#!/usr/bin/env python3
# encoding: utf-8
# author: Vincent
# refer: https://github.com/vc5

from bs4 import BeautifulSoup

from config import UserAgents
from .common import Job

# 店铺签到列表
SHOPSIGN_LIST = ['https://mall.jd.com/shopSign-1000081124.html',
                 'https://mall.jd.com/shopSign-1000092704.html',
                 'https://mall.jd.com/shopSign-146935.html',
                 'https://mall.jd.com/shopSign-22705.html',
                 'https://mall.jd.com/shopSign-199094.html',
                 'https://mall.jd.com/shopSign-77222.html',
                 'https://mall.jd.com/shopSign-86174.html',
                 'https://mall.jd.com/shopSign-1000001582.html',
                 'https://mall.jd.com/shopSign-1000003179.html',
                 'https://mall.jd.com/shopSign-1000000725.html',
                 'https://mall.jd.com/shopSign-708779.html',
                 'https://mall.jd.com/shopSign-1000003663.html',
                 'https://mall.jd.com/shopSign-1000002670.html',
                 'https://mall.jd.com/shopSign-1000001933.html'
                 ]


class ShopSign(Job):
    job_name = '店铺签到'
    UA = UserAgents['pc']
    index_url = 'https://mall.jd.com/shopSign-1000081124.html'
    login_url = index_url
    test_url = index_url
    is_mobile = False

    def sign(self):
        for url in SHOPSIGN_LIST:
            r = self.session.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            result_msg = ''
            try:
                shopname = soup.title.text.rstrip('  - 京东')
                if 'no-award' in soup.select('div.everyday-area')[0].attrs['class']:
                    result_msg = '本次未中奖'
                elif 'big-award' in soup.select('div.everyday-area')[0].attrs['class']:
                    result_msg = soup.select('div.everyday-area div.big')[0].get_text(strip=True)
                else:
                    result_msg = soup.select('div.everyday-area div.small')[0].get_text(strip=True)
                # result = soup.select('div.everyday-area')[0].get_text(strip=True)
                self.logger.info('店铺抽奖#{}#{}'.format(shopname, result_msg))
            except AttributeError:
                pass
        return True
