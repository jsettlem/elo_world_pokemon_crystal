import game_data_pb2 as _game_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattleBatch(_message.Message):
    __slots__ = ["battles"]
    BATTLES_FIELD_NUMBER: ClassVar[int]
    battles: _containers.RepeatedCompositeFieldContainer[BattleSummary]
    def __init__(self, battles: Optional[Iterable[Union[BattleSummary, Mapping]]] = ...) -> None: ...

class BattleSummary(_message.Message):
    __slots__ = ["enemy", "player", "seed", "turns", "winner"]
    class Winner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class TrainerID(_message.Message):
        __slots__ = ["instance", "trainer_class"]
        INSTANCE_FIELD_NUMBER: ClassVar[int]
        TRAINER_CLASS_FIELD_NUMBER: ClassVar[int]
        instance: int
        trainer_class: int
        def __init__(self, trainer_class: Optional[int] = ..., instance: Optional[int] = ...) -> None: ...
    class TurnDescriptor(_message.Message):
        __slots__ = ["enemy_mon", "player_mon", "selected_action", "selected_item", "selected_move", "selected_pokemon", "turn_number"]
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class BattleMon(_message.Message):
            __slots__ = ["hp", "max_hp", "party_index", "species"]
            HP_FIELD_NUMBER: ClassVar[int]
            MAX_HP_FIELD_NUMBER: ClassVar[int]
            PARTY_INDEX_FIELD_NUMBER: ClassVar[int]
            SPECIES_FIELD_NUMBER: ClassVar[int]
            hp: int
            max_hp: int
            party_index: int
            species: _game_data_pb2.PokemonSpecies
            def __init__(self, species: Optional[Union[_game_data_pb2.PokemonSpecies, str]] = ..., hp: Optional[int] = ..., max_hp: Optional[int] = ..., party_index: Optional[int] = ...) -> None: ...
        ENEMY_MON_FIELD_NUMBER: ClassVar[int]
        FORCE_SWITCH: BattleSummary.TurnDescriptor.Action
        ITEM: BattleSummary.TurnDescriptor.Action
        MOVE: BattleSummary.TurnDescriptor.Action
        PLAYER_MON_FIELD_NUMBER: ClassVar[int]
        SELECTED_ACTION_FIELD_NUMBER: ClassVar[int]
        SELECTED_ITEM_FIELD_NUMBER: ClassVar[int]
        SELECTED_MOVE_FIELD_NUMBER: ClassVar[int]
        SELECTED_POKEMON_FIELD_NUMBER: ClassVar[int]
        SWITCH: BattleSummary.TurnDescriptor.Action
        TURN_NUMBER_FIELD_NUMBER: ClassVar[int]
        enemy_mon: BattleSummary.TurnDescriptor.BattleMon
        player_mon: BattleSummary.TurnDescriptor.BattleMon
        selected_action: BattleSummary.TurnDescriptor.Action
        selected_item: _game_data_pb2.ItemIdentifier
        selected_move: _game_data_pb2.MoveIdentifier
        selected_pokemon: int
        turn_number: int
        def __init__(self, turn_number: Optional[int] = ..., selected_action: Optional[Union[BattleSummary.TurnDescriptor.Action, str]] = ..., selected_move: Optional[Union[_game_data_pb2.MoveIdentifier, str]] = ..., selected_item: Optional[Union[_game_data_pb2.ItemIdentifier, str]] = ..., selected_pokemon: Optional[int] = ..., player_mon: Optional[Union[BattleSummary.TurnDescriptor.BattleMon, Mapping]] = ..., enemy_mon: Optional[Union[BattleSummary.TurnDescriptor.BattleMon, Mapping]] = ...) -> None: ...
    DRAW_BY_EXCEPTION: BattleSummary.Winner
    DRAW_BY_TURN_COUNT: BattleSummary.Winner
    ENEMY: BattleSummary.Winner
    ENEMY_FIELD_NUMBER: ClassVar[int]
    PLAYER: BattleSummary.Winner
    PLAYER_FIELD_NUMBER: ClassVar[int]
    SEED_FIELD_NUMBER: ClassVar[int]
    TURNS_FIELD_NUMBER: ClassVar[int]
    WINNER_FIELD_NUMBER: ClassVar[int]
    enemy: BattleSummary.TrainerID
    player: BattleSummary.TrainerID
    seed: str
    turns: _containers.RepeatedCompositeFieldContainer[BattleSummary.TurnDescriptor]
    winner: BattleSummary.Winner
    def __init__(self, seed: Optional[str] = ..., player: Optional[Union[BattleSummary.TrainerID, Mapping]] = ..., enemy: Optional[Union[BattleSummary.TrainerID, Mapping]] = ..., winner: Optional[Union[BattleSummary.Winner, str]] = ..., turns: Optional[Iterable[Union[BattleSummary.TurnDescriptor, Mapping]]] = ...) -> None: ...
