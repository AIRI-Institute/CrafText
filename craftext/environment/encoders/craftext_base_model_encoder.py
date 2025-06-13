import os
from enum import Enum
from abc import ABC, abstractmethod


os.environ['HF_HOME'] = "."


class EncodeForm(Enum):
    """
    Enum representing different forms of encoding.
    """
    TOKEN = "token" # Tokenized form of the instruction
    EMBED_CONCAT_ALL = "embed_concat_all"  # Concatenated embeddings of all tokens
    EMBED_CONCAT_NO_STOPWORDS = "embed_concat_no_stopwords"  # CLS embeddings of all tokens excluding stopwords
    EMBED_CLS_FOR_SPLITS = "embed_cls_for_splits"  # CLS embeddings for each split
    EMBEDDING = "default" # Default embedding form, typically CLS embeddings

class EncodeModel(ABC):
    def __init__(self, form_to_use=EncodeForm.EMBEDDING):
        """
        Abstract base class for encoding models.
        """
        self.form_to_use = form_to_use

    @abstractmethod
    def encode(self, instruction):
        """
        Abstract method to encode an instruction.
        Must be implemented in a concrete class.
        """
        pass

    @abstractmethod
    def get_embeddings(self, instruction):
        """
        Abstract method to get embeddings.
        Must be implemented in a concrete class.
        """
        pass

    @abstractmethod
    def get_tokens(self, instruction):
        """
        Abstract method to get tokens.
        Must be implemented in a concrete class.
        """
        pass


