from scrapy.cmdline import execute
import sys
import os

print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","imdb"])

# path = os.path.dirname(os.path.abspath(__file__))+"/result/"
# i=0
# with open(path+str(i)+".txt",'r') as f:
#     for line in f.readlines():
#         line=line.rstrip("\n")
#         print(line)