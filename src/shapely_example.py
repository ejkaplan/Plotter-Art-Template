import shapely
import elkplot
import numpy as np

rng = np.random.default_rng()

def cloud(n_circles: int, width: float, height: float, margin: float) -> shapely.LineString:
    lines = []
    for _ in range(n_circles):
        r = rng.uniform(0.5, 1)
        center = shapely.Point(*rng.uniform(margin+r, (width-margin-r, height-margin-r)))
        lines.append(center.buffer(r))
    return shapely.union_all(lines).exterior

def main():
    width, height, margin = 7, 5, 0.5
    layers = [cloud(30, width, height, margin) for _ in range(3)]
    drawing = shapely.GeometryCollection(layers)
    drawing = elkplot.optimize(drawing)
    elkplot.draw(drawing, width, height, plot=False)


if __name__ == "__main__":
    main()
