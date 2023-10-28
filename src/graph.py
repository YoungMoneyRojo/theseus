class IndoorNav:
    def __init__():
        pass

    class Feature:
        def __init__(self, name, id, path: str):
            self.name = name
            self.id = id
            self.path = path
        
    class Landmark(Feature):
        def __init__(self, name, id):
            super().__init__(name, id)


    class Edge():
        pass