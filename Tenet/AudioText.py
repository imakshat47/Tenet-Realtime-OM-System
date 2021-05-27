try:
    from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError
    from datetime import datetime
    from time import sleep
    import threading
    from Tenet.Super import BaseClass
    from Tenet.Sentiment import SentimentScore
except Exception as e:
    exit("Library Exception in AudioText: ", e)


class Listner(BaseClass):
    def __init__(self):
        self._check_debug("Listner"+self._class_init_msg)
        self.__recognizer = Recognizer()
        self.__mic = Microphone()
        self._sentimeter = SentimentScore()
        self._show(self._available_device_msg)
        for _mic_name in self.__mic.list_microphone_names():
            self._show(" - "+_mic_name, "\n", False)
        self._show(self._background_noise_msg)
        with self.__mic as noise:
            self.__recognizer.adjust_for_ambient_noise(
                noise, duration=self._noise_check_duration)
        self._show("Noise Adjusting"+self._process_complete_msg)
        self._text = ''
        self._polarity = 0

    ''' Audio to text converter '''

    def _audio_to_text(self, audio, _recognizer):
        _text = ""
        try:
            # _text = _recognizer.recognize_google(audio)            
            _text = self.__recognizer.recognize_google(audio)
        except UnknownValueError:
            self._show(self._unknown_err)
        # except RequestError:
        #     self._show(self._request_err)
        except: 
            self._show("Exception!!")
        self._debug("Text Collected: "+_text)
        return _text

    ''' Callback for _listen_in_background() '''

    def __callback(self, _recognizer, audio):
        try:
            self._threads()
            _text = self._audio_to_text(audio, _recognizer)        
            self._polarity = self._sentimeter._score(_text)
        except:
            print(self._slow_internet_err)
        self._text += _text
        self._polarity = self._sentimeter._score(self._text)

    ''' Active Threads via threading '''

    def _threads(self):
        # self._show("Thread List: "+threading.enumerate())
        self._debug("Current Thread: "+str(threading.current_thread()) +
                   " | Active Count: "+str(threading.active_count()))

    ''' Listen in background '''

    def _listen_in_background(self):
        try:
            self._debug("Listen in Background: ")
            self._show(self._listening_msg)
            stop_listening = self.__recognizer.listen_in_background(
                self.__mic, self.__callback)
            while True:
                self._threads()
                self._sleep(self._listen_in_background_sleep)
        except KeyboardInterrupt:
            self._show("Keyboard Interrupt!!")
            pass
        stop_listening(wait_for_stop=True)
        self._debug("Text Collected: "+self._text)
        self._polarity = self._sentimeter._score(self._text)
        self._debug("Listner"+self._process_complete_msg)
