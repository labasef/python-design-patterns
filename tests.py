from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Class that defines the interface for the strategy.
    """
    def __init__(self, data: str):
        self._data = data

    def __call__(self):
        self.prepare_data()
        self.analyze_data()
        self.report_data()

    def __enter__(self):
        print("Entering the strategy")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the strategy")
        return True

    @abstractmethod
    def prepare_data(self):
        pass

    @abstractmethod
    def analyze_data(self):
        pass

    @abstractmethod
    def report_data(self):
        pass


class AnalyseLetters(Strategy):

    def prepare_data(self):
        self._data = self._data.upper()

    def analyze_data(self):
        self._data = self._data.replace(" ", "")
        self._data = list(self._data)

    def report_data(self):
        print("Reporting data", str(self._data))


with AnalyseLetters("Hello World") as analyse:
    analyse()