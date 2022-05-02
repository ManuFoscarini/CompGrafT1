class Objects:
    listObjects = []

    @staticmethod
    def clear_cache():
        Objects.listObjects = []

    @staticmethod
    def add(element):
        Objects.listObjects.append(element)