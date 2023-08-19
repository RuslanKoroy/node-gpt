from scripts.classes import Node


class InputNode(Node):
    def __init__(self, name):
        super().__init__(name, node_type=InputNode)
        self.outputs: list = []


class OutputNode(Node):
    def __init__(self, name):
        super().__init__(name, node_type=OutputNode)
        self.inputs: list = []


class TextProcessingNode(Node):
    def __init__(self, name):
        super().__init__(name, node_type=TextProcessingNode)
        self.inputs: list = []
        self.outputs: list = []


class GenerativeNode(Node):
    def __init__(self, name):
        super().__init__(name, node_type=GenerativeNode)
        self.inputs: list = []
        self.outputs: list = []
