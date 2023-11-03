# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:49:32 2017

@author: davirami
"""
from icrawler.builtin import GoogleImageCrawler
import os
import random

path = 'Path/to/Save/Photos/'
keyword='your query to search images'

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': path})

try:
    google_crawler.crawl(keyword=keyword, max_num=100,
                         min_size=(400, 200), max_size=None)
except Exception as e:
    print(f"An error occurred: {e}")

files = os.listdir(path)
for file in files:
    new_filename = str(random.randint(2000000, 2999999)) + '.jpg'
    new_file_path = os.path.join(path, new_filename)
    
    while os.path.exists(new_file_path):
        new_filename = str(random.randint(2000000, 2999999)) + '.jpg'
        new_file_path = os.path.join(path, new_filename)
    
    os.rename(os.path.join(path, file), new_file_path)
    print(new_filename)