import svgwrite

# note a maximum of 16 colors are supported(as svg size is 16 *16)
colors = [((187, 145, 144), (237, 183, 182)), ((187, 185, 184), (237, 234, 233)), ((175, 28, 39), (225, 36, 50)), ((192, 48, 54), (242, 60, 68)), ((197, 78, 82), (247, 97, 102)), ((193, 110, 112), (243, 138, 141))]
dwg = svgwrite.Drawing('sample.svg', profile='full')

for i in range(len(colors)):
    print(colors[i][0][0], colors[i][0][1], colors[i][0][2])
    dwg.add(dwg.line((0, 0+i), (16, 0+i), stroke=svgwrite.rgb(colors[i][0][0], colors[i][0][1], colors[i][0][2], '%')))

dwg.save()