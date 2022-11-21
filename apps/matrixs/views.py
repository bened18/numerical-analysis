import json
from django.views.generic import TemplateView

from apps.matrixs.functions.Cholesky import cholesky

from apps.interpolations.functions.convert_string_to_type import convert_string_to_list
from apps.matrixs.functions.GaussSeidel import gaussSeidel


def convert_string_to_list(string1):
    res = f"[{string1}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json


def convert_string_to_list_individual(string1):
    res = f"[{string1}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json

class CholeskyTemplateView(TemplateView):
    template_name = "matrixs/Cholesky.html"
    
    def get_context_data(self, **kwargs):
        context = super(CholeskyTemplateView,
                        self).get_context_data(**kwargs)
        
        matrix_a = self.request.GET.get('a', '') # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        
        if matrix_a:
            matrix = convert_string_to_list(matrix_a)        
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

    def get_context_data(self, **kwargs):
        context = super(GaussSeidelTemplateView,
                        self).get_context_data(**kwargs)
        
        matrix_a = self.request.GET.get('A', '') # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_b = self.request.GET.get('B', '') # [1,1,1,1]
        matrix_x0 = self.request.GET.get('x0', '') # [0,0,0,0]
        itermax = self.request.GET.get('itermax', '') # 100
        tolerance = self.request.GET.get('tolerance', '') #0.00000007
        
        if matrix_a and matrix_b and matrix_x0 and itermax and tolerance:
            
            itermax = int(itermax)
            tolerance = float(tolerance)
            
            matrix_a = convert_string_to_list_individual(matrix_a)
            matrix_b = convert_string_to_list_individual(matrix_b)
            matrix_x0 = convert_string_to_list_individual(matrix_x0) 
        
            context["result"] = gaussSeidel(matrix_a, matrix_b, matrix_x0, itermax, tolerance)
        
        return context
    
    
    
    
    
class JacobiTemplateView(TemplateView):
    template_name = "matrixs/Jacobi.html"
    
class LUwithGaussianSimpleEliminationTemplateView(TemplateView):
    template_name = "matrixs/LUwithGaussianSimpleElimination.html"
    
class LUWithPartialPivotingTemplateView(TemplateView):
    template_name = "matrixs/LUWithPartialPivoting.html"


class SorTemplateView(TemplateView):
    template_name = "matrixs/Sor.html"
