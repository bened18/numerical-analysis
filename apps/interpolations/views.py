from django.views.generic import TemplateView


class CubicSplineTemplateView(TemplateView):
    template_name = "interpolations/CubicSpline.html"


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
