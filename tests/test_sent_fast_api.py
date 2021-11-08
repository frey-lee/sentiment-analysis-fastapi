from sent_fast_api import __version__
from sent_fast_api.model import SentimentModel


def test_version():
    assert __version__ == "0.1.0"


def test_model():
    model = SentimentModel()
    polarity, subjectivity = model.get_sentiment("I love you three thousand")
    polarity = round(polarity, 1)
    subjectivity = round(subjectivity, 1)
    assert polarity <= 1
    assert polarity >= -1
    assert subjectivity <= 1
    assert subjectivity >= 0
