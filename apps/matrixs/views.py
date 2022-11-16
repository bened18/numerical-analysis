from django.views.generic import TemplateView


class CholeskyTemplateView(TemplateView):
    template_name = "matrixs/Cholesky.html"


class CroutTemplateView(TemplateView):
    template_name = "matrixs/Crout.html"


class DoolittleTemplateView(TemplateView):
    template_name = "matrixs/Doolittle.html"


class GaussianEliminationWithPartialPivotingTemplateView(TemplateView):
    template_name = "matrixs/GaussianEliminationWithPartialPivoting.html"


class GaussianEliminationWithTotalPivotingTemplateView(TemplateView):
    template_name = "matrixs/GaussianEliminationWithTotalPivoting.html"


class GaussianSimpleEliminationTemplateView(TemplateView):
    template_name = "matrixs/GaussianSimpleElimination.html"
    
class GaussSeidelTemplateView(TemplateView):
    template_name = "matrixs/GaussSeidel.html"
    
class JacobiTemplateView(TemplateView):
    template_name = "matrixs/Jacobi.html"
    
class LUwithGaussianSimpleEliminationTemplateView(TemplateView):
    template_name = "matrixs/LUwithGaussianSimpleElimination.html"
    
class LUWithPartialPivotingTemplateView(TemplateView):
    template_name = "matrixs/LUWithPartialPivoting.html"


class SorTemplateView(TemplateView):
    template_name = "matrixs/Sor.html"
