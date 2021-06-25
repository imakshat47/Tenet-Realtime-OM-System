from textblob import TextBlob
from Tenet.Super import BaseClass
import pickle
import sklearn


class SentimentScore(BaseClass):
    def __init__(self):
        self._debug("Sentiment Score"+self._class_init_msg)

    ''' Print Ordinals '''

    def __ordinals(self, _score):
        if _score > 0:
            if _score < 0.35:
                return self._ordinal_1
            else:
                return self._ordinal_2
        elif _score < 0:
            if _score > -0.35:
                return self._ordinal_3
            else:
                return self._ordinal_4
        else:
            return self._ordinal_0

    ''' Preforms Sentiment Score Generator '''

    def _score(self, _txt='', _global=False):
        try:
            __txtBlob = TextBlob(_txt)
            __text = str(__txtBlob.correct())
            self._check_debug("Intermediate Corrected Text: "+__text)
            _sentiment_score = round(
                TextBlob(__text).sentiment.polarity, self._sentiment_score_round_of_digit)
            if _global:
                self._show("!! Sentimeter Output: "+self.__ordinals(_sentiment_score) +
                           " [ Score: "+str(_sentiment_score)+" ]")
            else:
                self._show(self._sentimeter_msg +
                           self.__ordinals(_sentiment_score))
        except:
            self._show("Textblob"+self._status_err_msg)
        return _sentiment_score

    def _ssg(self, text=''):
        try:
            vectorizer = pickle.load(
                open(self._pickle_dir + 'vectorizer.sav', 'rb'))
            classifier = pickle.load(
                open(self._pickle_dir + 'classifier.sav', 'rb'))
            text_vector = vectorizer.transform([text])
            score_class = classifier.predict(text_vector)
        except:
            self._show("SSG"+self._status_err_msg)
        return score_class
