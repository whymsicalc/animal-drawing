import cs1graphics as cg

def make_paper():
    paper = cg.Canvas(600, 600, bgColor="skyBlue", title="Cat")
    return paper

paper = make_paper()


class Cat:
    center_x = None
    center_y = None
    color = None

    def __init__(self, center_point_x, center_point_y, color):
        self.center_x = center_point_x
        self.center_y = center_point_y
        self.color = color

    def make_cat_appear(self):
        cat = cg.Circle(100, cg.Point(self.center_x, self.center_y))
        cat.setFillColor(self.color)
        eye1 = cg.Circle(10, cg.Point(self.center_x - 50, self.center_y - 25))
        eye1.setFillColor("black")
        eye2 = cg.Circle(10, cg.Point(self.center_x + 50, self.center_y - 25))
        eye2.setFillColor("black")
        ear1 = cg.Polygon(cg.Point(self.center_x - 75, self.center_y - 75), cg.Point(self.center_x - 50, self.center_y - 50), cg.Point(self.center_x - 50, self.center_y - 75))
        nose = cg.Polygon(cg.Point(self.center_x - 25, self.center_y - 25), cg.Point(self.center_x, self.center_y), cg.Point(self.center_x + 25, self.center_y - 25))
        nose.setFillColor("yellow")
        ear1.setDepth(25)
        nose.setDepth(25)
        paper.add(nose)
        # paper.add(ear1)
        paper.add(cat)
        paper.add(eye1)
        paper.add(eye2)


fluffy = Cat(300,300, "Blue")
fluffy.make_cat_appear()
