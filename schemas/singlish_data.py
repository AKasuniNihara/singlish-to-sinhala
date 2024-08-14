from pydantic import BaseModel

class singlish_data(BaseModel):
    singlish_sentence:str
    sinhala_sentence:str
    correctness:str
