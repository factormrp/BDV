from pydantic import BaseModel

class Series(BaseModel):
    category : str
    name : str
    id : str

    def __str__(self):
        return self.name
