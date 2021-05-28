# import Tenet.var as var
from time import sleep

''' Base Class '''


class BaseClass(object):

    """ Setting Environment Variables """
    # debuger
    _print_active = True
    _debuger_active = True
    _development_env = True

    # AudioText Class
    _sleep_time = 1.5
    _noise_check_duration = 2
    _listen_in_background_sleep = 90
    _background_noise_msg = "Adjusting for Background Noise!!\nA moment of silence, Please..."
    _available_device_msg = "Available Devices: "

    _listening_msg = "Listening..."

    _unknown_err = "Oops! Didn't catch that..."
    # _request_err = "Seems unstable Internet!!"
    # # File System
    _audio_files_dir = "dataset/audio/"
    _text_files_dir = "dataset/text/"
    
    # SentimentScore
    _ordinal_0 = "  😁   Neutral"
    _ordinal_1 = "  😊   Good"
    _ordinal_2 = "  😀   Very Good "
    _ordinal_3 = "  😌   Bad"
    _ordinal_4 = "  😓   Very Bad"

    _sentiment_score_round_of_digit = 3

    _sentimeter_msg = "!! Sentimeter: "

    # Global msg
    _slow_internet_err = "Uh oh! Couldn't Request Results. Slow Internet!!"

    _class_init_msg = " Class Initiated!!"
    _class_desctruct_msg = " Class Destructed!!"

    _status_succ_msg = " Request Success!!"
    _status_err_msg = " Request Error!!"

    _process_complete_msg = " Process Completed!!"

    ''' Constructor '''

    def __init__(self):
        self._development_env and print("Super"+self._class_init_msg)

    ''' Print data on screen'''

    def _show(self, _txt="", end="\n", _sleep = True):
        _sleep and sleep(self._sleep_time)  # short sleep
        self._print_active and print(_txt, end=end)
        _sleep and sleep(self._sleep_time)  # short sleep

    ''' Print for Activated Debugger '''

    def _debug(self, _txt=""):
        sleep(self._sleep_time)  # short sleep
        self._debuger_active and print(_txt)
        sleep(self._sleep_time)  # short sleep

    ''' Print for Developer Environment '''

    def _check_debug(self, _txt=""):
        sleep(self._sleep_time)  # short sleep
        self._development_env and print(_txt)
        sleep(self._sleep_time)  # short sleep

    ''' Sleep for time @ _sleep_time '''
    def _sleep(self, _sleep_time):
        sleep(_sleep_time)
