from django.views.generic import TemplateView

from apps.interpolations.functions.CubicSpline import traza3natural
from apps.interpolations.functions.Lagrange import lagrange
from apps.interpolations.functions.LinealSpline import lineal_spline
from apps.interpolations.functions.NewtonInterpolation import newton
from apps.interpolations.functions.QuadraticSpline import quadratic
from apps.interpolations.functions.Vandermonde import vandermonde


class CubicSplineTemplateView(TemplateView):
    template_name = "interpolations/CubicSpline.html"
    def get_context_data(self, **kwargs):
        context = super(CubicSplineTemplateView,
                        self).get_context_data(**kwargs)

        xi = self.request.GET.get('xi', '')
        fi = self.request.GET.get('fi', '')

        if xi and fi:            
            context['polynomial_result'] = traza3natural(xi, fi)[0]
            context['section_result'] = traza3natural(xi, fi)[1]

        return context


class LagrangeTemplateView(TemplateView):
    template_name = "interpolations/Lagrange.html"
    def get_context_data(self, **kwargs):
        context = super(LagrangeTemplateView,
                        self).get_context_data(**kwargs)
        xi = self.request.GET.get('xi', '')
        fi = self.request.GET.get('fi', '')
        
        l_dict = lagrange(xi, fi)
        
        if xi and fi:
            context["fi"] = l_dict["fi"]
            context["dividers"] = l_dict["dividers"]
            context["lagrangePolynomialExpresion"] = l_dict["lpe"]
            context["lagrangePolynomial"] = l_dict["lp"]
            context["xi"] = l_dict["xi"]
            context["pxi"] = l_dict["pxi"]
            context["pfi"] = l_dict["pfi"]
        
        return context


class LinealSplineTemplateView(TemplateView):
    template_name = "interpolations/LinealSpline.html"
    def get_context_data(self, **kwargs):
        context = super(LinealSplineTemplateView,
                        self).get_context_data(**kwargs)
        xi = self.request.GET.get('xi', '')
        fi = self.request.GET.get('fi', '')
        if xi and fi:            
            context['result'] = lineal_spline(xi, fi)
        return context

class NewtonInterpolationTemplateView(TemplateView):
    template_name = "interpolations/NewtonInterpolation.html"
    def get_context_data(self, **kwargs):
        context = super(NewtonInterpolationTemplateView,
                        self).get_context_data(**kwargs)
        xi = self.request.GET.get('xi', '')
        fi = self.request.GET.get('fi', '')
        print(xi, fi)
        if xi and fi:            
            context['tablaDD'] = newton(xi, fi)[0]
            context['coeficientes'] = newton(xi, fi)[1]
            context['polynomial_result'] = newton(xi, fi)[2]


class QuadraticSplineTemplateView(TemplateView):
    template_name = "interpolations/QuadraticSpline.html"
    def get_context_data(self, **kwargs):
        context = super(QuadraticSplineTemplateView,
                        self).get_context_data(**kwargs)
        xi = self.request.GET.get('xi', '')
        fi = self.request.GET.get('fi', '')
        if xi and fi:            
            context['result'] = quadratic(xi, fi)


class VandermondeTemplateView(TemplateView):
    template_name = "interpolations/Vandermonde.html"
    def get_context_data(self, **kwargs):
        context = super(VandermondeTemplateView,
                        self).get_context_data(**kwargs)
        xi = self.request.GET.get('xi', '')
        fi = self.request.GET.get('fi', '')
        if xi and fi:            
            context['result'] = vandermonde(xi, fi)
