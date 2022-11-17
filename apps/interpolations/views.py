from django.views.generic import TemplateView

from apps.interpolations.functions.CubicSpline import traza3natural
from apps.interpolations.functions.Lagrange import lagrange
from apps.interpolations.functions.LinealSpline import lineal_spline


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
        if xi and fi:
            context["activate"] = lagrange()
        
        return context


class LinealSplineTemplateView(TemplateView):
    template_name = "interpolations/LinealSpline.html"
    def get_context_data(self, **kwargs):
        context = super(CubicSplineTemplateView,
                        self).get_context_data(**kwargs)

        xi = self.request.GET.get('xi', '')
        fi = self.request.GET.get('fi', '')

        if xi and fi:            
            context['polynomial_result'] = lineal_spline(xi, fi)[0]
            context['section_result'] = lineal_spline(xi, fi)[1]

        return context

class NewtonInterpolationTemplateView(TemplateView):
    template_name = "interpolations/NewtonInterpolation.html"


class QuadraticSplineTemplateView(TemplateView):
    template_name = "interpolations/QuadraticSpline.html"


class VandermondeTemplateView(TemplateView):
    template_name = "interpolations/Vandermonde.html"
