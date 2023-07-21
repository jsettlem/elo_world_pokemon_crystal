from dataclasses import dataclass, field
from typing import List, Union, Optional, Literal

from protobuf.battle_pb2 import BattleSummary


@dataclass
class Pokémon:
	level: int
	species: str
	hasCustomMoves: bool = False
	moves: Optional[List[str]] = None
	held_item: Optional[str] = None


@dataclass
class Trainer:
	class_id: int
	instance_id: int
	class_name: str
	name: str
	rematch: int
	dvs: List[int]
	gender: str
	switch_style: str
	strategy: List[str]
	pokémon: List[Pokémon]
	items: List[str]

	elo: int = 0
	rank: int = 0
	wins: int = 0
	losses: int = 0
	battles: List['Battle'] = field(default_factory=list)
	victories: List['Battle'] = field(default_factory=list)
	defeats: List['Battle'] = field(default_factory=list)

	has_later_rematch: bool = False

	tier: str = ""

	continent: Optional[str] = None
	area: Optional[str] = None
	game_index: Optional[int] = None

	is_unused: bool = False
	is_rematch: bool = False

	@property
	def full_name(self) -> str:
		return f"{self.class_name} {self.name}{'#' + str(self.rematch) if self.rematch > 1 or self.has_later_rematch else ''}"

	@property
	def average_level(self):
		return sum(p.level for p in self.pokémon) / len(self.pokémon)

	@property
	def pokemon_have_moves(self) -> bool:
		return any(p.moves for p in self.pokémon)

	@property
	def pokemon_have_items(self) -> bool:
		return any(p.held_item for p in self.pokémon)

	@property
	def dv_total(self) -> int:
		return sum(self.dvs)

	@property
	def gender_symbol(self) -> str:
		return {
			"MALE": "♂",
			"FEMALE": "♀",
			"ENBY": "⚥"
		}[self.gender]

@dataclass
class Battle:
	seed: str
	player: Trainer
	enemy: Trainer
	winner: str
	winning_trainer: Trainer
	losing_trainer: Trainer
