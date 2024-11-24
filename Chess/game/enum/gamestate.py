from enum import Enum


class GameState(Enum):
    ACTIVE = "active"
    WHITE_WIN = "white_win"
    BALCK_WIN = "black_win"
    RESIGNED = "resign"
    ABORT = "abort"