import re


class StringProcessor:
    """
    This class represents a StringProcessor.

    Attributes:

    input_str (str): The string to be preprocessed.
    """

    def __init__(self, input_str: str):
        self.input_str = input_str

    def remove_asterisk(self) -> None:
        """Removes the asterisk from the text."""
        self.input_str = self.input_str.replace("*", "")

    def remove_hashtag(self) -> None:
        """Removes the hashtag from the text."""
        self.input_str = self.input_str.replace("#", "")

    def remove_triple_dot(self) -> None:
        """Removes triple dots from the text."""
        self.input_str = self.input_str.replace("…", "")

    def convert_special_characters_to_english(self) -> None:
        """Converts special characters."""
        self.input_str = self.input_str.replace("–", "-")
        self.input_str = self.input_str.replace("|", "")

    def convert_german_unit_to_english(self) -> None:
        """Converts special characters."""
        self.input_str = self.input_str.replace("μ", "mu")
        self.input_str = self.input_str.replace("10^9", "nm")
        self.input_str = self.input_str.replace("10^6", "mum")
        self.input_str = self.input_str.replace("10^12", "pm")

    def remove_legend(self) -> None:
        """Removes map numbers."""
        self.input_str = re.sub(r"\([0-9]\)", " ", self.input_str)

    def convert_to_lowercase(self) -> None:
        """Converts the input string to lowercase."""
        self.input_str = self.input_str.lower()

    @staticmethod
    def process_string(raw_text: str) -> str:
        """Preprocess the string in several steps and returns it."""
        processor = StringProcessor(raw_text)
        processor.remove_asterisk()
        processor.remove_hashtag()
        processor.remove_triple_dot()
        processor.convert_special_characters_to_english()
        processor.convert_german_unit_to_english()
        processor.remove_legend()
        preprocessed_text = processor.input_str
        return preprocessed_text
