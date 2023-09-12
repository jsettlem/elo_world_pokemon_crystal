from random import Random
from typing import Iterable, List

from pyboy import PyBoy
from pyboy.utils import WindowEvent

from constants import buttons
from constants.memory import MemoryAddress, reverse_symbols

frame_limit = 60 * 60 * 10

def get_value(emulator: PyBoy, address: "MemoryAddress") -> bytearray:
    return bytearray([emulator.get_memory_value(address.offset + i) for i in range(address.size)])

def set_value(emulator: PyBoy, source: Iterable[int], address: "MemoryAddress") -> None:
    for i, value in enumerate(source):
        if i >= address.size:
            break
        emulator.set_memory_value(address.offset + i, value)

def copy_values(source: PyBoy, source_address: "MemoryAddress", target: PyBoy, target_address: "MemoryAddress") -> None:
    assert source_address.size == target_address.size
    set_value(target, get_value(source, source_address), target_address)


def randomize_rdiv(emulator: PyBoy, rng: "Random"):
    random_clock = [rng.randint(0, 255) for _ in range(4)]
    emulator.mb.timer.dividers = random_clock


def byte_to_pyboy_input(button: int) -> WindowEvent:
    match button:
        case buttons.A_BUTTON:
            return WindowEvent.PRESS_BUTTON_A
        case buttons.B_BUTTON:
            return WindowEvent.PRESS_BUTTON_B
        case buttons.UP_BUTTON:
            return WindowEvent.PRESS_ARROW_UP
        case buttons.DOWN_BUTTON:
            return WindowEvent.PRESS_ARROW_DOWN
        case buttons.LEFT_BUTTON:
            return WindowEvent.PRESS_ARROW_LEFT
        case buttons.RIGHT_BUTTON:
            return WindowEvent.PRESS_ARROW_RIGHT
        case _:
            return WindowEvent.PASS


def byte_to_pyboy_release(last_button):
    match last_button:
        case buttons.A_BUTTON:
            return WindowEvent.RELEASE_BUTTON_A
        case buttons.B_BUTTON:
            return WindowEvent.RELEASE_BUTTON_B
        case buttons.UP_BUTTON:
            return WindowEvent.RELEASE_ARROW_UP
        case buttons.DOWN_BUTTON:
            return WindowEvent.RELEASE_ARROW_DOWN
        case buttons.LEFT_BUTTON:
            return WindowEvent.RELEASE_ARROW_LEFT
        case buttons.RIGHT_BUTTON:
            return WindowEvent.RELEASE_ARROW_RIGHT
        case _:
            return WindowEvent.PASS



def run_until_breakpoint(emulator: PyBoy, breakpoints: List[str], demo: bytearray = bytearray(), ):
    emulator.mb.breakpoints_list = []
    for bp in breakpoints:
        emulator.mb.add_breakpoint(*reverse_symbols[bp])

    emulator.override_memory_value(rom_bank=0x0e, addr=0x5791 - 0x4000, value=0x0) # fix cal

    frame = 0
    while not emulator.tick() and frame < frame_limit:
        emulator.set_memory_value(addr=0xc664, value=0x0) # disable exp gain

        frame += 1
        if frame < len(demo):
            if frame > 0 and demo[frame - 1] != demo[frame]:
                emulator.send_input(byte_to_pyboy_release(demo[frame - 1]))
            emulator.send_input(byte_to_pyboy_input(demo[frame]))

    if frame >= frame_limit:
        raise Exception("Timeout reached")
