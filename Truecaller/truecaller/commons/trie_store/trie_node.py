class TrieNode:
    def __init__(self):
        self.characters = [None] * 256
        self.completion_status = False

        # This is only populated at comp
        self.node_values = []