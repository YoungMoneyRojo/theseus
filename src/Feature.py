class Feature:
    def __init__(self, name, id, imgPath: str):
        self.name = name
        self.id = id
        self.imgPath = imgPath

    def __eq__(self, other):
        return (self.name == other.name)

