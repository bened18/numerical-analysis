from django.views.generic import TemplateView

from apps.interpolations.functions.CubicSpline import inputcubic


class CubicSplineTemplateView(TemplateView):
    template_name = "interpolations/CubicSpline.html"

    def get_context_data(self, **kwargs):
        context = super(CubicSplineTemplateView,
                        self).get_context_data(**kwargs)

        inputx1 = self.request.GET.get('xi', '')
        inputf1 = self.request.GET.get('fi', '')

        if inputx1 and inputf1:

            functionresult = inputcubic(inputx1, inputf1)

            context['result'] = f"{functionresult}"

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
