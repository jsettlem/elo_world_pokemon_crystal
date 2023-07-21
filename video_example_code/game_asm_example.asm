AI_Smart_Ohko:
; Dismiss this move if player's level is higher than enemy's level.
; Else, discourage this move is player's HP is below 50%.

    ld a, [wBattleMonLevel]
    ld b, a
    ld a, [wEnemyMonLevel]
    cp b
    jp c, AIDiscourageMove
    call AICheckPlayerHalfHP
    ret c
    inc [hl]
    ret


    
ld a, [$c639]
ld b, a
ld a, [$d213]
cp b
jp c, $5503
call $526e
ret c
inc [hl]
ret


