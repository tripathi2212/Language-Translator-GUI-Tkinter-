import goslate


text = raw_input("Say something:\n")

gs = goslate.Goslate()
New = gs.translate(text,'hi')
New1 = gs.translate(text,'fr')
New2 = gs.translate(text,'ar')
New3 = gs.translate(text,'bn')

print New
print New1
print New2
print New3

