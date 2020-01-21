import imageio
images = []
filenames = ["#1.PNG", "#2.PNG", "#3.PNG", "#4.PNG", "#5.PNG", "#6.PNG", "#7.PNG", "#8.PNG", "#9.PNG", "#10.PNG"]
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('animate.gif', images, duration=0.2)