# import Tenet.var as var
from time import sleep
import threading
import Tenet.setup as setup

''' Base Class '''


class BaseClass(object):

    """ Setting Environment Variables """
    # Module Vars
    # debuger
    _development_env = True and setup._development_env
    _debuger_active = True and setup._debuger_active

    # AudioText Class
    _sleep_time = 1.5
    _noise_check_duration = 2
    _listen_in_background_sleep = int(60*3) # For 3min
    _background_noise_msg = "Adjusting for Background Noise!!\nA moment of silence, Please..."
    _available_device_msg = "Available Devices: "

    _listening_msg = "Listening..."

    # _unknown_err = "Oops! Didn't catch that..."
    _unknown_err = "No Audio Input..."
    # _request_err = "Seems unstable Internet!!"
    # # File System
    _audio_files_dir = "dataset/audio/"
    _text_files_dir = "dataset/text/"

    # SentimentScore
    _ordinal_0 = " 😁 Neutral"
    _ordinal_1 = " 😊 Good"
    _ordinal_2 = " 😀 Very Good "
    _ordinal_3 = " 😌 Bad"
    _ordinal_4 = " 😓 Very Bad"

    _sentiment_score_round_of_digit = 3

    _sentimeter_msg = "!! Sentimeter: "

    # Global Vars
    _print_active = True

    # Global msg
    _slow_internet_err = "Uh oh! Couldn't Request Results. Slow Internet!!"

    _class_init_msg = " Class Initiated!!"
    _class_desctruct_msg = " Class Destructed!!"

    _status_succ_msg = " Request Success!!"
    _status_err_msg = " Request Error!!"

    _process_complete_msg = " Process Completed!!"

    # Processing
    _processing_count = 6
    _interval = 0.8

    ''' Constructor '''

    def __init__(self):
        self._development_env and print("Super"+self._class_init_msg)

    ''' Print data on screen'''

    def _show(self, _txt="", end="\n", _sleep=True):
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

    ''' Output System Details on screen '''

    def _out_msg(self, msg):
        print("|======================================================|")
        print("|    TENET: Realtime Threaded Opinion Mining System    |")
        print("|======================================================|\n")
        self._out_processing(self._processing_count)
        self._show(msg, "\n", False)

    ''' Shows Processing on screen '''

    def _out_processing(self, _count):
        for _ in range(_count):
            self._show("-- --  -- -- -- --  -- --  -- --  -- --  -- --  -- -- -|", '\r', False)
            self._sleep(self._interval)
            self._show("|-- --- --- --- --- --- --- --- --- --- --- --- --- ---|", '\r', False)
            self._sleep(self._interval)
            self._show("|//////////////////////////////////////////////////////|", '\r', False)
            self._sleep(self._interval)
            self._show("||||||||||||||||||||||||||||||||||||||||||||||||||||||||", '\r', False)
            self._sleep(self._interval)
            self._show("|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|", '\r', False)
            self._sleep(self._interval)
            self._show("|------------------------------------------------------|", '\r', False)
            self._sleep(self._interval)
        self._show("|======================================================|", "\n", False)        


    ''' Active Threads via threading '''

    def _threads(self):
        # self._show("Thread List: "+threading.enumerate())
        if self._development_env == True:
            _thread_name = str(threading.current_thread())
        else:
            _thread_name = str(threading.current_thread().name)
        self._debug("Current Thread: "+_thread_name +
                    " | Active Count: "+str(threading.active_count()))
