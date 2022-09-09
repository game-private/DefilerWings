#!/usr/bin/env python
# coding=utf-8
from characters import Romeo
from utils import call
from pythoncode import girls_data

class love(object):
    def __init__(self,game_ref):
        self.game = game_ref

    def new_love_smuggler(self): # Девушка находит свою истинную лбовь
        self.game.girl.love = Romeo(game_ref=self.game,type='smuggler')
        call("lb_new_love_smuggler")

    def new_love_lizardman(self): # Девушка находит свою истинную лбовь
        self.game.girl.love = Romeo(game_ref=self.game,type='lizardman')
        call("lb_new_love_lizardman")
#        self.game.girls_list.event('new_love_lizardman')

    @property
    def is_trade_possible(self):
# Возвращает возможность продажи
        assert self.game.girl, "Girl not found"
        caravan_trade = self.game.historical_check('caravan_trade')
        trade_possible = caravan_trade and not self.game.girl.virgin and self.game.girl.pregnant == 0 and not self.game.girl.type == 'mermaid' and not self.game.girl.blind and not self.game.girl.cripple and not girls_data.girls_info[self.game.girl.type]['giantess']
        return trade_possible


