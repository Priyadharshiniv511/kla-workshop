# -*- coding: utf-8 -*-
"""ML1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1raEx_PESQlCMM5N91X8iIlIQ93Kis_a2
"""

import yaml
import logging
import logging.config

with open('M1A_Workflow.yml','r') as file:
    data=yaml.safe_load(file)
    
print(data)

logging.basicConfig(filename= "C:\\Users\\Priyadharshini\\Desktop\\logfile1.log",filemode='w',level=logging.INFO)
logger=logging.getLogger()

logger=logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
file_handler = logging.FileHandler('file1.log')
formatter=logging.Formatter('%(asctime)s ; %(Task)s : %(function)s : %(entry)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logging.info('your text goes here')