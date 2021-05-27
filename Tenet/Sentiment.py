from textblob import TextBlob
from Tenet.Super import BaseClass


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

    def _score(self, _txt=''):
        try:
            __txtBlob = TextBlob(_txt)
            _sentiment_score = round(TextBlob(str(
                __txtBlob.correct())).sentiment.polarity, self._sentiment_score_round_of_digit)
            self._show(self._sentimeter_msg+self.__ordinals(_sentiment_score) +
                       " [ Score: "+str(_sentiment_score)+" ]")
        except:
            self._show("Textblob"+self._status_err_msg)
        return _sentiment_score