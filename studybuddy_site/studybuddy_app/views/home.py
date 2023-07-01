from django.views.generic.base import TemplateView
# https://docs.djangoproject.com/en/4.2/ref/class-based-views/base/#django.views.generic.base.TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["latest_articles"] = Article.objects.all()[:5]
        return context