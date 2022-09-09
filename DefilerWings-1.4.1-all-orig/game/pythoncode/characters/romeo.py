# coding=utf-8

import random
from pythoncode.utils import get_random_image
from pythoncode import data
from talker import Talker

class Romeo(Talker):
    def __init__(self,type,*args, **kwargs):
        # Инициализируем родителя
        super(Romeo, self).__init__(*args, **kwargs)
#        self.game = game_ref
        if type == 'smuggler':
          self.avatar = get_random_image(u"img/avahuman/thief")
          self.name = "%s" % (random.choice(data.thief_first_names))
        elif type == 'lizardman':          
          self.avatar = get_random_image(u"img/avahuman/lizardman")
          self.name = "%s" % (random.choice(data.lizardman_names))
        self.type=type
        

