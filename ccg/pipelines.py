# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import string
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline

class CardImagePipeline(ImagesPipeline):
# Accomplishes goal of original code; puts cards in subdirectories
# based on card type
    def file_path(self, request, response=None, info=None):
        testpath = request.url.split('/')[-3]
        testfile = request.url.split('/')[-1]
        testtarget = testpath + "/" + testfile
        return testtarget

class SameDirImagesPipeline(ImagesPipeline):
# Fork: Puts all cards in one directory, uses type as
# first part of file name, separated by space hyphen space
    def file_path(self, request, response=None, info=None):
        testpath = request.url.split('/')[-3]
        testfile = request.url.split('/')[-1]
        testtarget = testpath + " - " + testfile
        return testtarget