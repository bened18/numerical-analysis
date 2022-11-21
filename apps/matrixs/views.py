from django.views.generic import TemplateView

from apps.matrixs.functions.Cholesky import cholesky


class CholeskyTemplateView(TemplateView):
    template_name = "matrixs/Cholesky.html"
    
    def get_context_data(self, **kwargs):
        context = super(CholeskyTemplateView,
                        self).get_context_data(**kwargs)
        
        matrix = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
        
        print(cholesky(matrix))
        
        context["result"] = cholesky(matrix)
        
        return context
    



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
