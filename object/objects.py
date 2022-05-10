class Objects:
    listObjects = []
    selectedObject = None
    numberObjects = 1

    @staticmethod
    def clear_cache():
        Objects.listObjects = []

    @staticmethod
    def add(element):
        Objects.listObjects.append(element)
        Objects.numberObjects += 1

    @staticmethod
    def select_object(objectLabel):
        for object in Objects.listObjects:
            if (object.label == objectLabel):
                Objects.selectedObject = object
                break

    @staticmethod
    def clearSelectObject():
        Objects.selectedObject = None