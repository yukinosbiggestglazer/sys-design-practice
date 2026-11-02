class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


class Server:
    def __init__(self):
        self.objects = {"calc": Calculator()}

    def handle_request(self, obj_name, method_name, args):
        obj = self.objects[obj_name]
        method = getattr(obj, method_name)
        return method(*args)


class ClientStub:
    def __init__(self, server, obj_name):
        self.server = server
        self.obj_name = obj_name

    def call(self, method_name, *args):
        print(f"Client: calling {method_name}{args}")
        result = self.server.handle_request(self.obj_name, method_name, args)
        print(f"Client: received result {result}")
        return result


server = Server()
stub = ClientStub(server, "calc")
stub.call("add", 5, 3)
stub.call("multiply", 4, 6)
