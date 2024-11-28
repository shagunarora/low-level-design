from LLD.Elevator.entities.floor import Floor
from LLD.Elevator.entities.lift.lift import Lift
from LLD.Elevator.services.lift_service import LiftService


def main():
    # Create lifts
    lift_service = LiftService()

    # Insert new lifts in lift service.
    lift1 = Lift()
    lift2 = Lift()
    lift3 = Lift()
    
    lift_service.add_lift(lift1)
    lift_service.add_lift(lift2)
    lift_service.add_lift(lift3)

    # Request lift from various floors to some destination floor.
    floor1 = Floor(1)
    floor2 = Floor(2)
    floor3 = Floor(3)

    floor1.request_lift(2)
    floor2.request_lift(-1)
    floor3.request_lift(4)
    