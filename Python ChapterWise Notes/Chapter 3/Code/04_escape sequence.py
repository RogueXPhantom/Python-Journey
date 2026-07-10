# \n → New Line
a = "Harry is a good boy\nbut not a bad boy."
print(a)  # Harry is a good boy
          # but not a bad boy.

# \t → Tab
a = "Harry\tis\ta\tgood\tboy."
print(a)  # Harry    is    a    good    boy.

# \\ → Backslash
a = "C:\\Users\\Harry"
print(a)  # C:\Users\Harry

# \" → Double Quote
a = "Harry is a good \"boy\"."
print(a)  # Harry is a good "boy".

# \' → Single Quote
a = 'It\'s Harry.'
print(a)  # It's Harry.

# \r → Carriage Return
a = "Hello\rHi"
print(a)  # Hi

# \b → Backspace
a = "Helloo\b"
print(a)  # Hello

# \a → Bell
a = "Hello\a"
print(a)  # Hello

# \f → Form Feed
a = "Hello\fWorld"
print(a)  # Hello 
          #      World

# \v → Vertical Tab
a = "Hello\vWorld"
print(a)  # Hello 
          #      World

# \0 → Null Character
a = "Hello\0World"
print(a)  # Hello World

# \xhh → Hexadecimal Character
a = "\x48\x65\x6C\x6C\x6F"
print(a)  # Hello

# \ooo → Octal Character
a = "\110\145\154\154\157"
print(a)  # Hello

# \uXXXX → Unicode Character
a = "Omega: \u03A9"
print(a)  # Omega: Ω

# \UXXXXXXXX → Unicode Emoji
a = "Smile: \U0001F600"
print(a)  # Smile: 😀