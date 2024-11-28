from LLD.Elevator.entities.lift.lift_direction import LiftDirection


class Display:
    def __init__(self, floor=0, direction=None):
        self.floor = floor
        self.direction = direction
    
    def set_floor(self, floor):
        self.floor = floor
    
    def set_direction(self, direction):
        self.direction = direction

    def display(self):
        if self.direction == LiftDirection.NOT_MOVING:
            print(f"Lift is idle and currently is on {self.floor}")
            return
        
        print(f"Lift is moving {self.direction} and currently is on {self.floor}")
