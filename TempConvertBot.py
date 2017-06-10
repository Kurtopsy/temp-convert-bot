#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 21:23:54 2017

@author: u/Kurtopsy
"""

import praw
import pdb
import re
import os



FAHRENHEIT_REPLY_MESSAGE = "In Celsius, that's: "
CELSIUS_REPLY_MESSAGE = "In Fahrenheit, that's: "


tempType = []
tempNum = []

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
   with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))
    
print("Obtaining 25 comments...")
with open("posts_replied_to.txt", "a") as f:
    for comment in reddit.subreddit('TempConvertBot').comments(limit=25):
        if "!*" in comment.body:
            print('String with "!*" found in comment {}'.format(comment.id))
            tempType = comment.body[-1:]
            tempNum = comment.body[3:-1]
            if comment.id not in posts_replied_to:
                if 'f' in tempType or 'F' in tempType:
                    convertedNum = (int(tempNum) - 32) * 5/9
                    celsius = (str(convertedNum))
                    comment.reply(FAHRENHEIT_REPLY_MESSAGE + celsius + "C")
                    print("Replied to comment " + comment.id)
                    f.write(comment.id + "\n")
                    f.close
                elif 'c'in tempType or 'C' in tempType:
                    convertedNum = (int(tempNum) * 9/5) + 32
                    fahrenheit = (str(convertedNum))
                    comment.reply(CELSIUS_REPLY_MESSAGE + fahrenheit + "F")
                    print("Replied to comment " + comment.id)
                    f.write(comment.id + "\n")
                    f.close