from src.llm import LLM

def test_llm():
    llm = LLM()
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
    response = llm.chat(messages)
    print(response)
    assert response is not None

def test_llm_get_models():
    llm = LLM()
    models = llm.get_models()
    print(models)
    assert models is not None