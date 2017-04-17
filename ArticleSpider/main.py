import os
import sys

from scrapy.cmdline import execute

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

execute(["scrapy", "crawl", "jobbole"])
