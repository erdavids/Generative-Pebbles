
square_size = 100
square_count = 12
square_rows = 17

w = square_size/2 * (square_count + 2)
h = square_size/2 * (square_rows + 2)

ran_rot = .005

colors = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]

def setup():
    size(w, h)
    global img
    img = createImage(w, h, ARGB)
    
    random_rotate = 0.0
    random_increase = .02
        
    translate(square_size, square_size)
    for i in range(square_rows):
        for j in range(square_count):
            pushMatrix()
            translate(square_size/2*j, i*square_size/2)
            c = colors[int(random(len(colors)))]
            print(c)
            print(c[0])
            fill(c[0], c[1], c[2])
            rotate(random(-i*(ran_rot+i*.003), i*(ran_rot+i*.003)))
            rect(-square_size/2, -square_size/2, square_size/2, square_size/2)
            popMatrix()

def draw():
    image(img, 0, 0)
