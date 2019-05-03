# serviceTranslate.py
from googletrans import Translator
class ServiceTranslate:
    def __init__(self):
        self.translator = Translator(service_urls=[
            'translate.google.com',
            'translate.google.cn',
        ])
    
    def t(self, theStrSlice, dest='zh-CN'):
       return self.translator.translate(theStrSlice, dest)
