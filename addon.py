#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xbmcswift2 import Plugin
from resources.lib import htmlscraper

plugin = Plugin()

@plugin.route('/')
def index():
    plugin.log.info("Calling index()")
    items = [{'label' : item['label'], 
              'path' : plugin.url_for(item['path'])} for item in htmlscraper.get_main_menu_continents()]

    return plugin.finish(items)

        
@plugin.route('/video1/')
def video1():
    items = [{
        'label': 'Hello XBMC!',
        'path': 'http://s3.amazonaws.com/KA-youtube-converted/JwO_25S_eWE.mp4/JwO_25S_eWE.mp4',
        'is_playable': True
    }]
    return plugin.finish(items)
       
             
            
