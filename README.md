This is a final task for Stepic Selenium course

Attention! 
1. This project uses f-strings that were introduced in Python 3.6
2. If you get the mistake like this 
   _________________________________________________________________ ERROR collecting test_main_page.py __________________________________________________________________
ImportError while importing test module 'C:\Users\Vasya\Downloads\AQA_Python_stepik_part_4-master\test_main_page.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
test_main_page.py:1: in <module>
    from .pages.main_page import MainPage
E   ImportError: attempted relative import with no known parent package

please delete dots "." before imports pages. Make imports like this
from pages.main_page import MainPage
3.  If you have any other promblems please look at requirements.txt and set all of the packages with command
   pip install -r requirements.txt
