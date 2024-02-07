from django.views.generic import ListView
from django.views.generic.edit import CreateView
from site_module.models import site_setting
from .forms import contactModelForms
from .models import UserProfile


# Create your views here.

class ContactUsView(CreateView):
    # or model = contact_us
    form_class = contactModelForms
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args , **kwargs)
        setting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context


def store_file(file):
    with open('temp/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    model = UserProfile
    template_name = 'contact_module/create_profile_page.html'
    fields = '__all__'
    success_url = '/contact-us/create-profile'
    # def get(self, request):
    #     form = ProfileForm()
    #     return render(request, 'contact_module/create_profile_page.html',{
    #         'form': form
    #     })
    #
    # def post(self, request):
    #     submitted_form = ProfileForm(request.POST, request.FILES)
    #     if submitted_form.is_valid():
    #     # store_file(request.FILES['image'])
    #         profile = UserProfile(image=request.FILES['user_image'])
    #         profile.save()
    #         return redirect('/contact-us/create-profile/')
    #     return render(request, 'contact_module/create_profile_page.html', {
    #         'form': submitted_form
    #     })


# class ContactUsView(FormView):
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = contactModelForms
#     success_url = '/contact-us'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class ContactUsView(View):
#
#     def get(self, request):
#         Contact_forms = contactModelForms()
#         return render(request, 'contact_module/contact_us_page.html', {
#             'Contact_forms': Contact_forms
#         })
#
#     def post(self, request):
#         Contact_forms = contactModelForms(request.POST)
#         if Contact_forms.is_valid():
#             Contact_forms.save()
#             return redirect('index_page')
#

# def contact_us_page(request):
#     if request.method == 'POST':
#         # Contact_forms = contact_forms(request.POST)
#         Contact_forms = contactModelForms(request.POST)
#         if Contact_forms.is_valid():
#             Contact_forms.save()
#             return redirect('index_page')
#     else:
#         # else = request.method == 'GET'
#         # Contact_forms = contact_forms()
#         Contact_forms = contactModelForms()
#     return render(request, 'contact_module/contact_us_page.html', {
#         'Contact_forms': Contact_forms
#     })

class ProfileListView(ListView):
    template_name = 'contact_module/profile_list_page.html'
    model = UserProfile
    context_object_name = 'profiles'
