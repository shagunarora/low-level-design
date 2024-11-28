from LLD.Elevator.entities.lift.lift_state import LiftState


class MovingDownState(LiftState):
    def add_requests(self, floors, current_floor):
        for floor in floors:
            continue