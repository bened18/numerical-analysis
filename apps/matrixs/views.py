from django.views.generic import TemplateView


class CubicSplineTemplateView(TemplateView):
    template_name = "matrixs/Cholesky.html"


class LagrangeTemplateView(TemplateView):
    template_name = "matrixs/Crout.html"


class LinealSplineTemplateView(TemplateView):
    template_name = "matrixs/Doolittle.html"


class NewtonInterpolationTemplateView(TemplateView):
    template_name = "matrixs/GaussianEliminationWithPartialPivoting.html"


class QuadraticSplineTemplateView(TemplateView):
    template_name = "matrixs/GaussianEliminationWithTotalPivoting.html"


class VandermondeTemplateView(TemplateView):
    template_name = "matrixs/GaussianSimpleElimination.html"
    
class VandermondeTemplateView(TemplateView):
    template_name = "matrixs/GaussSeidel.html"
    
class VandermondeTemplateView(TemplateView):
    template_name = "matrixs/Jacobi.html"
    
class VandermondeTemplateView(TemplateView):
    template_name = "matrixs/LUwithGaussianSimpleElimination.html"
    
class VandermondeTemplateView(TemplateView):
    template_name = "matrixs/LUWithPartialPivoting.html"


class VandermondeTemplateView(TemplateView):
    template_name = "matrixs/Sor.html"
