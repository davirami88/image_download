# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:49:32 2017

@author: davirami
"""
from icrawler.builtin import GoogleImageCrawler
import numpy as np
import os

path = 'C:/Path/to/Save/Photos/'
keyword='your query to search images'

google_crawler = GoogleImageCrawler(parser_threads=50, downloader_threads=500,
                                    storage={'root_dir': path})
google_crawler.crawl(keyword=keyword, max_num=1000,
                     date_min=None, date_max=None,
                     min_size=(400, 200), max_size=None)

files = os.listdir(path)
i = 1

for file in files:
    #changes the names of the different pictures and transform them to .jpg
    os.rename(os.path.join(path, file), os.path.join(path, str(np.random.randint(2000000))+'.jpg'))
    i = i+1
    print(str(np.random.randint(2000000)))
