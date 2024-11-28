
import heapq
import threading
import time

from logging import info
from threading import Lock
from typing import List

from LLD.Elevator.entities.display import Display
from LLD.Elevator.entities.lift.lift_direction import LiftDirection
from LLD.Elevator.entities.lift.lift_state import LiftState

from LLD.Elevator.entities.lift.lift_state.idle_state import IdleState
from LLD.Elevator.entities.lift.lift_state.moving_down_state import MovingDownState
from LLD.Elevator.entities.lift.lift_state.moving_up_state import MovingUpState
from LLD.Elevator.entities.request_command import RequestCommand

class Lift:
    def __init__(self, lift_id):
        self.lift_id = lift_id
        self.lock = Lock()
        self.lift_state = IdleState(self.lock)
        self.direction = LiftDirection.NOT_MOVING
        self.current_floor = 0

        # Min-heap (MOVING_UP State) / Max-heap (MOVING_DOWN State) to store 
        # requests in order of priority to process.
        self.requests_to_process = [] 
        self.display = Display()

        # Update display data.
        self.update_display()
    
    def move_to_floor(self, new_floor):
        
        print(f"Moving from floor {self.current_floor} to {new_floor}")
        time.sleep(2)  # Simulate the time taken to move to the floor

        with self.lock:
            self.current_floor = new_floor
        
    def update_display(self):
        # Update floor and direction in display object
        self.display.set_floor(self.current_floor)
        self.display.set_direction(self.direction)

        self.display.display()

    def handle_requests(self):
        while len(self.requests_to_process):
            # Pop the request with highest priority i.e. smallest distance.
            _, next_floor = heapq.heappop(self.requests_to_process)

            # TODO: we should only insert floors in request if that floor is not already
            # present in requests_to_process. Create a map to handle this.
            if next_floor == self.current_floor:
                continue

            if next_floor > self.current_floor:
                self.direction = LiftDirection.UP
                self.lift_state = MovingUpState(self.lock)
            else:
                self.direction = LiftDirection.DOWN
                self.lift_state = MovingDownState(self.lock)

            # Create two threads for moving to next floor and concurrently 
            # recalculating priorities for all remaining requests.
            move_thread = threading.Thread(target=self.move_to_floor, args=(next_floor,))
            recalculate_thread = threading.Thread(target=self.lift_state.recalculate_priorities, args=(self.requests_to_process, next_floor,))

            # Start both the threads
            move_thread.start()
            recalculate_thread.start()

            # Wait for both threads to complete before processing next request.
            move_thread.join()
            recalculate_thread.join()
        
        self.lift_state = IdleState()
        self.direction = LiftDirection.NOT_MOVING

    def add_request(self, floors):
        self.lift_state.add_request(floors, self.requests_to_process)

        if self.direction == LiftDirection.NOT_MOVING:
            self.handle_requests()
