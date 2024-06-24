from transformers import TextGenerationPipeline, GPT2LMHeadModel, AutoTokenizer
import torch
import os


class QuechuaModel:
    __model_path = os.path.abspath("./Modelo/story_generator_fined_tuned")
    __instance = None

    @staticmethod
    def getInstance():
        """Static access method."""
        if QuechuaModel.__instance == None:
            QuechuaModel()
        return QuechuaModel.__instance

    def __init__(self):
        """Virtually private constructor."""
        if QuechuaModel.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(self.__model_path)
            self.model = GPT2LMHeadModel.from_pretrained(self.__model_path, trust_remote_code=True)
            self.pipeline = TextGenerationPipeline(self.model, self.tokenizer)
            QuechuaModel.__instance = self

    def generate_text(
        self,
        prompt,
        max_length=150,
        do_sample=True,
        temperature=1.2,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.5,
    ):
        model_response = self.pipeline(
            prompt,
            max_length=max_length,
            do_sample=do_sample,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repetition_penalty=repetition_penalty,
        )

        return model_response[0]["generated_text"]
