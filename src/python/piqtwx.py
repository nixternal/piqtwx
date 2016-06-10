#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pi project to display Weather Underground observations and forecast
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
Query Weather Underground API and display the results in a clean, attractive,
and convenient way on an Adafruit PiTFT 2.8" display.
"""

import mainwindow_auto
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from wunderground import wunderground


class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.wg = wunderground()
        self.last_update = None
        self.update_weather()
        self.timer_clock = QtCore.QTimer(self)
        self.timer_clock.setInterval(1000)
        self.timer_clock.timeout.connect(self.display_time)
        self.timer_clock.start()
        self.timer_update_weather = QtCore.QTimer(self)
        self.timer_update_weather.setInterval(60000)
        self.timer_update_weather.timeout.connect(self.update_weather)
        self.timer_update_weather.start()
        # self.showFullScreen()

    def display_time(self):
        self.text_clock.setText(QtCore.QDateTime.currentDateTime().toString())

    def update_weather(self):
        self.wg.get_json_data()
        self.wg.parse_observation_data()
        self.wg.parse_forecast_data()
        w = self.wg.observation_dict
        f = self.wg.forecast_dict
        try:
            if w['observation_epoch'] != self.last_update:
                self.last_update = w['observation_epoch']
                # Observation Section
                pix = QPixmap('/home/pi/piqtwx/icons/%s' % w['icon'])
                self.icon_current.setPixmap(pix)
                self.text_current_temp_f.setText(
                    '<span style="color:#feae3c;">'
                    '<b>%s</b><sup>&deg;F</sup>'
                    '</span>' % w['temp_f']
                )
                self.text_wind_dir.setText(w['wind_dir'])
                self.text_wind_speed.setText(
                    '<b>%s</b>' % w['wind_mph']
                )
                if w['heat_index_f'] == 'NA' and w['windchill_f'] == 'NA':
                    self.label_hi_or_wc.setText('HI:')
                    self.text_hi_or_wc.setText('<b>NA</b>')
                elif w['heat_index_f'] != 'NA':
                    self.label_hi_or_wc.setText('HI:')
                    self.text_hi_or_wc.setText(
                        '<b>%s</b>&deg;F' % w['heat_index_f']
                    )
                else:
                    self.label_hi_or_wc.setText('WC:')
                    self.text_hi_or_wc.setText(
                        '<b>%s</b>&deg;F' % w['windchill_f']
                    )
                self.text_dewpoint.setText(
                    '<b>%s</b>&deg;F' % w['dewpoint_f']
                )
                self.text_humidity.setText(
                    '<b>%s</b>' % w['relative_humidity']
                )
                self.text_pressure.setText(
                    '<b>%s</b> in.' % w['pressure_in']
                )
                self.text_visibility.setText(
                    '<b>%s</b> miles' % w['visibility_mi']
                )
                if w['precip_today_in'] != "":
                    self.text_precip.setText(
                        '<b>%s</b> in.' % w['precip_today_in']
                    )
                else:
                    self.text_precip.setText(
                        '<b>0.0</b> in.'
                    )

                # Forecast Section
                self.text_forecast1_date.setText(
                    '<b>%s %s/%s</b>' % (
                        f[0]['weekday'],
                        f[0]['month'],
                        f[0]['day']
                    )
                )
                self.text_forecast1_temp.setText(
                    '<b style="color:#feae3c;">%s&deg;</b>'
                    '<span style="color:#aaa;"> | </span>'
                    '<b style="color:#0074a2;">%s&deg;</b>' % (
                        f[0]['high_f'],
                        f[0]['low_f']
                    )
                )
                pix = QPixmap('/home/pi/piqtwx/icons/%s' % f[0]['icon'])
                self.icon_forecast1.setPixmap(pix.scaledToWidth(40))

                self.text_forecast2_date.setText(
                    '<b>%s %s/%s</b>' % (
                        f[1]['weekday'],
                        f[1]['month'],
                        f[1]['day']
                    )
                )
                self.text_forecast2_temp.setText(
                    '<b style="color:#feae3c;">%s&deg;</b>'
                    '<span style="color:#aaa;"> | </span>'
                    '<b style="color:#0074a2;">%s&deg;</b>' % (
                        f[1]['high_f'],
                        f[1]['low_f']
                    )
                )
                pix = QPixmap('/home/pi/piqtwx/icons/%s' % f[1]['icon'])
                self.icon_forecast2.setPixmap(pix.scaledToWidth(40))

                self.text_forecast3_date.setText(
                    '<b>%s %s/%s</b>' % (
                        f[2]['weekday'],
                        f[2]['month'],
                        f[2]['day']
                    )
                )
                self.text_forecast3_temp.setText(
                    '<b style="color:#feae3c;">%s&deg;</b>'
                    '<span style="color:#aaa;"> | </span>'
                    '<b style="color:#0074a2;">%s&deg;</b>' % (
                        f[2]['high_f'],
                        f[2]['low_f']
                    )
                )
                pix = QPixmap('/home/pi/piqtwx/icons/%s' % f[2]['icon'])
                self.icon_forecast3.setPixmap(pix.scaledToWidth(40))
        except KeyError:
            # Current Observations
            pix = QPixmap('/home/pi/piqtwx/icons/unknown.png')
            self.icon_current.setPixmap(pix)
            self.text_current_temp_f.setText('<b>??</b><sup>&deg;F</sup>')
            self.text_hi_or_wc.setText('<b>???</b>&deg;F')
            self.text_dewpoint.setText('<b>???</b>&deg;F')
            self.text_humidity.setText('<b>???</b>%')
            self.text_pressure.setText('<b>???</b> in.')
            self.text_visibility.setText('<b>???</b> miles')
            self.text_precip.setText('<b>???</b> in.')

            # Forecast
            self.text_forecast1_date.setText('<b>???</b>')
            self.icon_forecast1.setPixmap(pix)
            self.text_forecast1_temp.setText(
                '<b style="color:#feae3c;">???&deg;</b>'
                '<span style="color:#aaa;"> | </span>'
                '<b style="color:#0074a2;">???&deg;</b>'
            )
            self.text_forecast2_date.setText('<b>???</b>')
            self.icon_forecast2.setPixmap(pix)
            self.text_forecast2_temp.setText(
                '<b style="color:#feae3c;">???&deg;</b>'
                '<span style="color:#aaa;"> | </span>'
                '<b style="color:#0074a2;">???&deg;</b>'
            )
            self.text_forecast3_date.setText('<b>???</b>')
            self.icon_forecast3.setPixmap(pix)
            self.text_forecast3_temp.setText(
                '<b style="color:#feae3c;">???&deg;</b>'
                '<span style="color:#aaa;"> | </span>'
                '<b style="color:#0074a2;">???&deg;</b>'
            )
            return False
        return True


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
