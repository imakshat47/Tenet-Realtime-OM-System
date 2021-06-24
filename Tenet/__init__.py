#!/usr/bin/env python3

"""
    Library to preform realtime opinion mining
"""

from Tenet.AudioText import Listner


__author__ = "Imakshat47"
__version__ = "1.2.3"
__license__ = "GNU"


class Models(Listner):

    def __init__(self):
        self._out_msg("System Ready!!")
        self._check_debug("Model"+self._class_init_msg)
        self._listner = Listner()

    def __del__(self):
        self._out_msg("System Closed!!")
        self._check_debug("Model"+self._class_desctruct_msg)

    def _model_(self):
        self._listner._listen_in_background()
        _moedel_output = self._check_debug(
            "Model"+self._process_complete_msg)
        print(_moedel_output)
