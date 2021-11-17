# import colorgram
#
# colors = colorgram.extract('painting.jpg', 30)

# color_list = []
#
# for _ in range(len(colors)):
#     rgb_color = tuple(colors[_].rgb)
#     color_list.append(rgb_color)
# print(color_list)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen

color_list = [(234, 251, 243), (197, 13, 32), (249, 237, 21), (39, 77, 188), (238, 227, 5), (39, 216, 68),
              (228, 160, 47), (243, 247, 253), (28, 40, 155), (214, 75, 14), (16, 153, 17), (199, 15, 11),
              (242, 34, 164), (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208), (11, 97, 62), (220, 160, 10),
              (18, 18, 43), (52, 211, 230), (11, 228, 239), (80, 73, 214), (238, 156, 217), (73, 212, 168),
              (81, 234, 202), (61, 233, 241), (5, 67, 42)]

tim = Turtle()

# paint 10x10 dots. 20 in size. spaced 50 paces apart.



Screen().exitonclick()
