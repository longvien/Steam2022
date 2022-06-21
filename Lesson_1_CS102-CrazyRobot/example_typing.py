import enum
from typing import Dict, List, Tuple

# --------------------------
# Basic (string, float, int)
# --------------------------
name: str = "Tay May"
weight: float = 60.2
age: int = 16

print(name)
print(weight)
print(age)

# --------------------------
# List
# --------------------------
thanhvien_cs102: List[str] = ["Tay May", "To Mo", "Robot"]
# có thể thay đổi giá trị
thanhvien_cs102[1] = "Hello"
print(thanhvien_cs102)

# --------------------------
# Tuple
# --------------------------
mytuple: Tuple[str, str, int] = ("Pygame", "with", 102)
# Không thể thay đổi giá trị
# mytuple[2] = 103
print(mytuple)

# --------------------------
# Dictionary
# --------------------------
card: Dict[str, str] = {"course": "CS102", "main": "Pygame"}
print(card["main"])


# --------------------------
# enum
# --------------------------
class GameStateType(enum.Enum):
    RUNNING = 0
    WON = 1
    LOST = 2


state: GameStateType = GameStateType.RUNNING
print(state == GameStateType.RUNNING)
print(state == GameStateType.WON)


# --------------------------
# Function
# --------------------------
def sum(items: List[float]) -> float:
    total: float = 0.0
    for item in items:
        total += item
    return total


danh_sach_diem: List[float] = [2.5, 1.5, 2, 3.25]
tong: float = sum(danh_sach_diem)

print(tong)
