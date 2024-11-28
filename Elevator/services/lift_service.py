from LLD.Elevator.commons.singleton_meta import SingletonMeta
from LLD.Elevator.entities.lift.lift import Lift
from LLD.Elevator.entities.request_command import RequestCommand
from LLD.Elevator.strategies.lift_selection_strategies.lift_selection_strategy import LiftSelectionStrategy


class LiftService(metaclass=SingletonMeta):
    def __init__(self, lift_selection_strategy: LiftSelectionStrategy):
        self.lifts = []
        self.lift_selection_strategy = lift_selection_strategy
    
    def process_request(self, request: RequestCommand):
        requesting_floor = request.requesting_floor
        destination_floor = request.destination_floor

        # Assign lift using lift selection strategy.
        lift: Lift = self.lift_selection_strategy.get_lift(requesting_floor, destination_floor)

        lift.add_request([requesting_floor, destination_floor])

