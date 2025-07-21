
from transformers import AutoModel, AutoTokenizer
import torch
import numpy as np
from craftext.environment.encoders.craftext_base_model_encoder import EncodeForm
import logging
# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class DistilBertEncode:
    def __init__(self, form_to_use=EncodeForm.EMBED_CONCAT_ALL, n_splits=1):
        """
        Unified implementation of DistilBERT encoder with multiple embedding options.
        """
        self.form_to_use = form_to_use
        model_name = "distilbert-base-uncased"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=".")
        self.model = AutoModel.from_pretrained(model_name, cache_dir=".")
        self.n_splits=n_splits
        self.stopwords = {"a", "an", "the", "in", "on", "at", "by", "to", "for", "of", "with", "and", "or", "but", "so"}  

    def encode(self, instruction):
        """
        Encodes the instruction based on the selected form_to_use.
        :param instruction: Text instruction.
        :param n_splits: Number of splits (used in EMBED_CLS_FOR_SPLITS mode).
        """
        n_splits=self.n_splits 
        if self.form_to_use == EncodeForm.TOKEN:
            return self.get_tokens(instruction)
        elif self.form_to_use == EncodeForm.EMBED_CONCAT_ALL:
            return self.get_concatenated_embeddings(instruction)
        elif self.form_to_use == EncodeForm.EMBED_CONCAT_NO_STOPWORDS:
            return self.get_concatenated_embeddings_no_stopwords(instruction)
        elif self.form_to_use == EncodeForm.EMBED_CLS_FOR_SPLITS:
            return self.get_cls_embeddings_for_splits(instruction, n_splits)
        else:
            return self.get_cls_embeddings(instruction)
        

    def get_concatenated_embeddings(self, instruction):
        """
        Generates a single embedding by concatenating embeddings of all tokens.
        """
        inputs = self.tokenizer(instruction, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        token_embeddings = outputs.last_hidden_state
        return token_embeddings.view(-1).numpy()

    def get_concatenated_embeddings_no_stopwords(self, instruction):
        """
        Generates a single embedding by concatenating embeddings of all tokens excluding stopwords.
        """
        tokens = self.tokenizer.tokenize(instruction)
        
        filtered_tokens = [t for t in tokens if t.lower() not in self.stopwords]
        
        inputs = self.tokenizer(filtered_tokens, return_tensors='pt', is_split_into_words=True)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        token_embeddings = outputs.last_hidden_state
        return token_embeddings.view(-1).numpy()
    
    def get_cls_embeddings(self, instructions):
        """
        Generates CLS embeddings for the given instruction.
        """
        
        inputs = self.tokenizer(
                instructions, 
                return_tensors='pt', 
                truncation=True, 
                padding=True, 
                max_length=50
            )
        
        with torch.no_grad():
                outputs = self.model(**inputs)
        cls_embeddings = outputs.last_hidden_state[:, 0, :]  
        concatenated_embedding = cls_embeddings.cpu().numpy() 
        return concatenated_embedding

    def get_cls_embeddings_for_splits(self, instructions, n_splits):
        """
        Generates CLS embeddings for the given instruction, splitting it into n_splits parts.
        """
        
        batch_embeddings = []

        for instruction in instructions:
           
            if instruction is None:
                instruction = 'None'
            words = instruction.split("\n")
            split_size = max(1, len(words) // n_splits)
            splits = [' '.join(words[i:i + split_size]) for i in range(0, len(words), split_size)]

           
            while len(splits) < n_splits:
                splits.append("")
            splits = splits[:n_splits]
       
            inputs = self.tokenizer(
                splits, 
                return_tensors='pt', 
                truncation=True, 
                padding=True, 
                max_length=50
            )
            
            logging.info("Batch encoding start")
      
            with torch.no_grad():
                outputs = self.model(**inputs)
            logging.info("Batch encoding end")

           
            cls_embeddings = outputs.last_hidden_state[:, 0, :]  
            concatenated_embedding = cls_embeddings.reshape(-1)  
            batch_embeddings.append(concatenated_embedding.cpu().numpy()) 

        return np.array(batch_embeddings)



    def get_tokens(self, instruction):
        """
        Generates tokens for the given instruction.
        """
        return self.tokenizer(instruction, max_length=30, truncation=True, padding="max_length", return_tensors='np')['input_ids']


def make_encoder(n_splits, form_to_use=EncodeForm.EMBED_CONCAT_ALL):
    class CustomBertEncodeModel(DistilBertEncode):
        def __init__(self, form_to_use=form_to_use):
            super().__init__(form_to_use=form_to_use, n_splits=n_splits)
    
    return CustomBertEncodeModel