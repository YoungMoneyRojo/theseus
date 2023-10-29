class Feature:
    def __init__(self, name, id=1, imgPath=""):
        self.name = name
        self.id = id
        self.imgPath = imgPath

    def __eq__(self, other):
        return (self.name == other.name)

