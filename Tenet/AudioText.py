try:
    from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError
    from datetime import datetime
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
        # local variables
        self._text = ''
        # for files
        self._file_middle = ""
        self._audio_file_extn = ".wav"
        self._text_file_extn = ".txt"



    ''' Audio to text converter '''

    def _audio_to_text(self, audio):
        _text = ""
        try:
            # _text = _recognizer.recognize_google(audio)
            _text = self.__recognizer.recognize_google(audio)
        except RequestError:
            self._show(self._slow_internet_err)
        except UnknownValueError:
            self._show(self._unknown_err)
        except:
            self._show("Exception!!")
        self._debug("Text Collected: "+_text)
        return _text



    ''' Callback for _listen_in_background() '''

    def __callback(self, _recognizer, audio):
        self._threads()
        self._write_to_file(self._audio_files_dir +
                            self._file_middle+self._audio_file_extn, audio)
        _text = self._audio_to_text(audio)
        self._polarity = self._sentimeter._score(_text)
        self._text += _text
        self._polarity = self._sentimeter._score(self._text)



    ''' Listen in background '''

    def _listen_in_background(self):
        try:
            self._file_middle = str(
                datetime.now().strftime('%Y-%m-%d_%H_%M_%S'))
            self._debug("Listen in Background: ")
            stop_listening = self.__recognizer.listen_in_background(
                self.__mic, self.__callback)
            while True:
                self._show(self._listening_msg)
                self._sleep(self._listen_in_background_sleep)
                self._threads()
        except KeyboardInterrupt:
            self._show("Keyboard Interrupt!!")
            pass
        stop_listening(wait_for_stop=True)
        self._debug("Text Collected: "+self._text)
        self._write_to_file(self._text_files_dir+self._file_middle +
                            self._text_file_extn, self._text, False, 'w')
        _polarity = self._sentimeter._score(self._text)
        self._debug("Listner"+self._process_complete_msg)
        print(self._text, str(_polarity), self._file_middle)
        return self._text, str(_polarity), self._file_middle



    ''' Write data content to file '''

    def _write_to_file(self, filename, data, _file_type_audio=True, mode='ab'):
        try:
            with open(filename, mode=mode) as file:
                if _file_type_audio:
                    file.write(data.get_wav_data())
                else:
                    file.write(data)
                    file.close()
            self._debug("File Done: "+filename)
        except Exception as e:
            self._show("Write to File Error!! "+filename)