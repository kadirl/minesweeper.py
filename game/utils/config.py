class Config:
    def __init__(self, **kwargs):
        self.params = kwargs
    
    def get(self, key, default=None):
        return self.params.get(key, default)
