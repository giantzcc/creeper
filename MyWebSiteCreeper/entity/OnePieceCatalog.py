# -*- coding: utf-8 -*-
class OnePieceCatalog(object):
    def __init__(self, episode, id, title, source):
        self.episode=episode
        self.id=id
        self.title=title
        self.source=source
    def __str__(self):
        return 'episode=%s,id=%s,title=%s'%(self.episode,self.id,self.title)