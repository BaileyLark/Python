section .text:

section .data: # variables
    message: db "Hello World!", 0xA #0xA is new line char 
    message_length: equ $-message   #$- is length  