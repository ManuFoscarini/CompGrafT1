class Objects:
    listObjects = []

    @staticmethod
    def clearObjects(object):
        Objects.listObjects = []

    @staticmethod
    def addObject(object):
        Objects.listObjects.append(object)
