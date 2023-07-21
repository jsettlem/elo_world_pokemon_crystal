struct Pokemon {
    int type1;
    int type2;
    int hp;
    int defense;
};

struct Move {
    int type;
    int power;
};


int checkTypeMatchup(int attackType, int targetType) {return 0;}

int calculatePokemonDamage(struct Pokemon* target, struct Move* attack) {
    int attackType = attack->type;
    int targetType = target->type1;

    int damageMultiplier = checkTypeMatchup(attackType, targetType);

    int damage = attack->power * damageMultiplier;
    damage /= target->defense;


    return target->hp - damage;
}
