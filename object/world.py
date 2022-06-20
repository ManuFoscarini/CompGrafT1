class World:
    listObjects = []
    selectedObject = None
    numberObjects = 1

    @staticmethod
    def clearObjects(object):
        World.listObjects = []

    @staticmethod
    def addObject(object):
        World.listObjects.append(object)
        World.numberObjects += 1

    @staticmethod
    def selectObject(objectLabel):
        for object in World.listObjects:
            if (object.label == objectLabel):
                World.selectedObject = object
                break

    @staticmethod
    def clearSelectObject():
        World.selectedObject = None
