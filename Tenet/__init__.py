#!/usr/bin/env python3

"""
    Library to preform realtime opinion mining
"""

from Tenet.AudioText import Listener


__author__ = "Imakshat47"
__version__ = "1.2.3"
__license__ = "GNU"


class Models(Listener):

    def __init__(self):
        self._out_msg("System Ready!!")
        self._check_debug("Model"+self._class_init_msg)
        self._listener = Listener()

    def __del__(self):
        self._out_msg("System Closed!!")
        self._check_debug("Model"+self._class_desctruct_msg)

    def _model_(self):
        self._listener._listen_in_background()
        self._check_debug(
            "Model"+self._process_complete_msg)
