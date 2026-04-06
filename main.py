# L-shape domain
from dolfin import *
from fenics import *
from mshr import *
import matplotlib.pyplot as plt

size = 10

class ExcludedRegion(SubDomain):
    def inside(self, x, on_boundary):
        return x[0] <= 0.5 and x[1] <= 0.5

mesh = RectangleMesh(Point(0, 0), Point(1, 1), size, size)
subdomains = MeshFunction("size_t", mesh, mesh.topology().dim())
subdomains.set_all(0)
excluded = ExcludedRegion()
excluded.mark(subdomains, 1)
mesh = SubMesh(mesh, subdomains, 0)

plot(mesh)