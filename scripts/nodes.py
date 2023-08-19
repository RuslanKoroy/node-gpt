from scripts.node_types import *


class ChatGPTNode(GenerativeNode):
    def __init__(self):
        super().__init__(name='ChatGPTNode')


class OpenAINode(GenerativeNode):
    def __init__(self):
        super().__init__(name='OpenAINode')


class PrintTextNode(OutputNode):
    def __init__(self):
        super().__init__(name='PrintTextNode')

    def run_node(self):
        for text in self.inputs:
            print(text)


class TextToList(TextProcessingNode):
    def __init__(self):
        self.input_count = 0
        self.roles = []

    def run_node(self):
        self.outputs.clear()
        for index, text in enumerate(self.inputs):
            self.outputs.append(
                {'content':text, 'role':self.roles[index]}
            )

