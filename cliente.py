class DatabaseClient:
    classmates = []
    connection = 0 

    def __init__(self, port) -> None:
        self.set_connection(port)

    def set_connection(self, port):
        self.connection = port

    def get_connection(self):
        return  self.connection

    def set_classmates(self, classmates):
        for classmate in classmates:
            self.classmates.append(classmates)
