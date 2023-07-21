calculatePokemonDamage:
  addiu $sp,$sp,-48
  sw $31,44($sp)
  sw $fp,40($sp)
  move $fp,$sp
  sw $4,48($fp)
  sw $5,52($fp)
  lw $2,52($fp)
  nop
  lw $2,0($2)
  nop
  sw $2,24($fp)
  lw $2,48($fp)
  nop
  lw $2,0($2)
  nop
  sw $2,28($fp)
  lw $5,28($fp)
  lw $4,24($fp)
  jal checkTypeMatchup
  nop

  sw $2,32($fp)
  lw $2,52($fp)
  nop
  lw $2,4($2)
  lw $3,32($fp)
  nop
  mult $3,$2
  mflo $2
  sw $2,36($fp)
  lw $2,48($fp)
  nop
  lw $2,12($2)
  lw $3,36($fp)
  nop
  div $0,$3,$2
  bne $2,$0,1f
  nop
  break 7
  mfhi $2
  mflo $2
  sw $2,36($fp)
  lw $2,48($fp)
  nop
  lw $3,8($2)
  lw $2,36($fp)
  nop
  subu $2,$3,$2
  move $sp,$fp
  lw $31,44($sp)
  lw $fp,40($sp)
  addiu $sp,$sp,48
  jr $31
  nop
