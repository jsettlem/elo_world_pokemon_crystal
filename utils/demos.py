import itertools
from typing import Iterable

from constants.file_paths import AI_DEMO
from utils.files import write_file
from constants import buttons as button, buttons as buttons


def make_button_sequence(buttons: Iterable[int]) -> Iterable[int]:
	zero = itertools.repeat(button.NOTHING_BUTTON)
	buffer_size = 12
	return [
		half_press
		for full_press in zip(zero, buttons, *([zero] * buffer_size))
		for half_press in full_press
	]


def generate_demo(buttons: Iterable[int], buffer_button: int = button.B_BUTTON, buffer_size: int = 10_000) -> bytearray:
	return bytearray([
		*make_button_sequence(buttons),
		*make_button_sequence([buffer_button] * buffer_size)
	])


def select_menu_item(current: int, target: int) -> Iterable[int]:
	if target < current:
		return [button.UP_BUTTON] * (current - target)
	else:
		return [button.DOWN_BUTTON] * (target - current)


def select_move(current_move: int, target_move: int) -> bytearray:
	return generate_demo([
		*buffer(3),
		button.B_BUTTON,
		button.UP_BUTTON,
		button.LEFT_BUTTON,
		button.A_BUTTON,
		*buffer(2),
		*select_menu_item(current_move, target_move),
		button.A_BUTTON
	])


def choose_pokemon(current: int, target: int) -> bytearray:
	return generate_demo([
		*buffer(3),
		*select_menu_item(current, target),
		button.A_BUTTON,
		*buffer(3),
		button.A_BUTTON
	])


def select_item(current, target) -> bytearray:
	return generate_demo([
		button.B_BUTTON,
		button.B_BUTTON,
		button.B_BUTTON,
		button.DOWN_BUTTON,
		button.LEFT_BUTTON,
		button.A_BUTTON,
		*buffer(5),
		button.A_BUTTON,
		*buffer(2),
		button.A_BUTTON,
		*buffer(5),
		# we don't need to select a Pokémon if it's an x-item, but the extra button inputs don't hurt anything
		*select_menu_item(current, target),
		button.A_BUTTON
	])


def buffer(length):
	return [button.NOTHING_BUTTON] * length


def select_switch(buffer_size=1) -> bytearray:
	return generate_demo([
		button.B_BUTTON,
		button.UP_BUTTON,
		button.RIGHT_BUTTON,
		button.A_BUTTON
	], buffer_button=button.NOTHING_BUTTON, buffer_size=buffer_size)


def generate_ai_demo() -> bytearray:
	return generate_demo([buttons.B_BUTTON, buttons.B_BUTTON, buttons.B_BUTTON, buttons.B_BUTTON, buttons.A_BUTTON, buttons.A_BUTTON,
							 buttons.B_BUTTON, buttons.B_BUTTON, buttons.A_BUTTON, buttons.DOWN_BUTTON, buttons.A_BUTTON,
							 buttons.B_BUTTON, buttons.B_BUTTON, buttons.A_BUTTON, buttons.DOWN_BUTTON, buttons.A_BUTTON,
							 buttons.B_BUTTON, buttons.B_BUTTON, buttons.A_BUTTON, buttons.DOWN_BUTTON, buttons.A_BUTTON])
