from openai import OpenAI
from typing import Optional, Dict, Any, List
from src.config import Config

class LLM:
    """
    LLM Class to inteacr with a vllm instance
    """

    def __init__(self,config: Optional[Dict[str, Any]] = None):
        """ init the LLM client
        Args:
            config (Optional[Dict[str, Any]]): LLM configuration dictionary.
        """
        self.config = config or Config().get("llm")
        self.client = OpenAI(api_key=self.config["api_key"],
                            base_url=self.config["base_url"])
        
    def chat(self,messages: List[Dict[str, str]]) -> str:
        """ chat with the LLM
        Args:
            messages (List[Dict[str, str]]): List of messages.
            
        Returns:
            str: Response from the LLM.
        """
        model_info = self.get_models()
        response = self.client.chat.completions.create(
            model=model_info["name"],
            messages=messages
        )
        return response.choices[0].message.content

    def get_models(self):
        """ get available models
        Returns:
            List[str]: List of available models.
        """
        models = self.client.models.list()
        return {'name': models.data[0].id, 
                'model_length': models.data[0].max_model_len, 
                'root': models.data[0].root}