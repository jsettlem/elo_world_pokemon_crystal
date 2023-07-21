import pickle
import zlib
from typing import List

from PIL import Image

from analysis_models.trainer import Trainer


victory_color = (0, 250, 113)
defeat_color = (134, 0, 0)

def main():
    print("loading augmented trainer data")
    with open("omega_augmented_trainer_list.pickle", "rb") as f:
        augmented_trainer_list: List[Trainer] = pickle.loads(zlib.decompress(f.read()))
    print("loaded")

    augmented_trainer_list.reverse()

    for i, trainer in enumerate(augmented_trainer_list):
        img = Image.new("RGB", (395, 2))
        for battle in trainer.victories:
            if battle.winning_trainer == battle.losing_trainer:
                continue
            if battle.losing_trainer.is_unused or battle.losing_trainer.is_rematch:
                continue

            was_player = battle.winner == "player"

            img.putpixel(
                xy = (battle.losing_trainer.game_index - 1, 0 if was_player else 1),
                value = victory_color
            )

        for battle in trainer.defeats:
            if battle.winning_trainer == battle.losing_trainer:
                continue

            if battle.winning_trainer.is_unused or battle.winning_trainer.is_rematch:
                continue

            was_player = battle.winner == "enemy"

            img.putpixel(
                xy = (battle.winning_trainer.game_index - 1, 0 if was_player else 1),
                value = defeat_color
            )

        if (not trainer.is_unused) and (not trainer.is_rematch):
            img.putpixel(
                xy = (trainer.game_index - 1, 0),
                value = (0, 0, 255)
            )

            img.putpixel(
                xy = (trainer.game_index - 1, 1),
                value = (0, 0, 255)
            )

        file_name = f"trainer_cards/win_records/{trainer.class_id}-{trainer.instance_id}.png"

        img.resize(size=(395 * 10, 2 * 10), resample=Image.NEAREST).save(file_name)

if __name__ == '__main__':
    main()
