
square_size = 50
square_count = 60
square_rows = 30

w = square_size/2 * (square_count + 2)
h = square_size/2 * (square_rows + 2)

ran_rot = .005
ran_mov = .02

colors = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]

def setup():
    size(w, h)
    global img
    img = createImage(w, h, ARGB)
    
    background(120, 120, 120)
    stroke(80, 80, 80)
    
    random_rotate = 0.0
    random_increase = .02
        
    translate(square_size, square_size)
    for i in range(square_rows):
        for j in range(square_count):
            pushMatrix()
            translate(j*square_size/2 + (i * random(-ran_mov, ran_mov)), i*square_size/2 + + (i * random(-ran_mov, ran_mov)))
            c = colors[int(random(len(colors)))]
            fill(c[0], c[1], c[2], 255)
            rotate(random(-i*(ran_rot+i*.003), i*(ran_rot+i*.003)))
            rect(-square_size/2, -square_size/2, square_size/2, square_size/2, )
            popMatrix()
    save("Examples/Pebbles-" + str(square_size) + "-" + str(square_count) + "x" + str(square_rows) + ".png")
def draw():
    image(img, 0, 0)
