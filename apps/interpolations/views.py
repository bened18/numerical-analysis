from django.views.generic import TemplateView

from apps.interpolations.functions.CubicSpline import traza3natural


class CubicSplineTemplateView(TemplateView):
    template_name = "interpolations/CubicSpline.html"
    def get_context_data(self, **kwargs):
        context = super(CubicSplineTemplateView,
                        self).get_context_data(**kwargs)

        xi = self.request.GET.get('xi', '')
        fi = self.request.GET.get('fi', '')

        if xi and fi:

            polynomial_result = traza3natural(xi, fi)[0]
            section_result = traza3natural(xi, fi)[1]

            context['polynomial_result'] = f"{polynomial_result}"
            context['section_result'] = f"{section_result}"

        return context


class LagrangeTemplateView(TemplateView):
    template_name = "interpolations/Lagrange.html"


class LinealSplineTemplateView(TemplateView):
    template_name = "interpolations/LinealSpline.html"


class NewtonInterpolationTemplateView(TemplateView):
    template_name = "interpolations/NewtonInterpolation.html"


class QuadraticSplineTemplateView(TemplateView):
    template_name = "interpolations/QuadraticSpline.html"


class VandermondeTemplateView(TemplateView):
    template_name = "interpolations/Vandermonde.html"
