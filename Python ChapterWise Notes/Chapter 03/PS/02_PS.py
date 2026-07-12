letter = ''' Dear <| Name|> 
<|Date|>           
            You are selected! '''

print(letter.replace("<| Name|>", "Rogue").replace("<|Date|>", "30 June 2027"))
