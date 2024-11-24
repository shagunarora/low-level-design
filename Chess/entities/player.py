class Player:
    def __init__(self, player_name, player_id):
        self.player_id = player_id
        self.player_name = player_name
        self.side_assigned = None
    
    def set_side_color(self, color):
        self.side_assigned = color
