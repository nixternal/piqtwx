#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Weather Underground current observation and forecast API for Pi Project
#
#  Copyright (c) 2016 Rich Johnson
#
#  Author: Rich Johnson <nixternal@gmail.com>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
#  USA.
"""
Query Weather Underground JSON and retrieve information pertaining to the
current observations as well as the future forecast.
"""

import configparser
import json
import urllib2

CONF_FILE = '/etc/default/piqtwx'

# Which data do you want to have available? Pick from the available JSON from
# Weather Underground
OBSERVATIONS_SET = [
    'observation_epoch',
    #  'icon_url',
    'icon',
    'temp_f',
    'relative_humidity',
    'wind_dir',
    'wind_mph',
    'pressure_in',
    'dewpoint_f',
    'heat_index_f',
    'windchill_f',
    'feelslike_f',
    'visibility_mi',
    'precip_today_in'
]


class wunderground:
    def __init__(self):
        self.observation_dict = dict()
        self.forecast_dict = []
        self.parse_config()

    def parse_config(self):
        config = configparser.ConfigParser()
        config.read(CONF_FILE)
        try:
            self.apikey = config.get('WUNDERGROUND', 'APIKEY')
            self.lang = config.get('WUNDERGROUND', 'LANG')
            self.pws = config.get('WUNDERGROUND', 'PWS')
        except KeyError:
            pass

    def get_json_data(self):
        try:
            f = urllib2.urlopen(
                'http://api.wunderground.com/api/%s'
                '/conditions/forecast10day/lang:%s'
                '/q/pws:%s.json' % (
                    self.apikey,
                    self.lang,
                    self.pws
                )
            )
        except urllib2.URLError:
            pass

        self.pjson = json.loads(f.read())

    def parse_observation_data(self):
        try:
            c_ob = self.pjson['current_observation']
        except KeyError:
            pass

        for ob in OBSERVATIONS_SET:
            self.observation_dict[ob] = c_ob[ob]

    def parse_forecast_data(self):
        try:
            f_ob = self.pjson['forecast']['simpleforecast']['forecastday']
        except KeyError:
            pass

        for i, forecast in enumerate(f_ob):
            conditions = {
                'day': forecast['date']['day'],
                'month': forecast['date']['month'],
                'weekday': forecast['date']['weekday'],
                'low_f': forecast['low']['fahrenheit'],
                'high_f': forecast['high']['fahrenheit'],
                'icon': forecast['icon']
            }
            self.forecast_dict.append(conditions)
