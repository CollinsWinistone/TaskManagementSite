from django.shortcuts import render
from client.forms import ClientRegistrationForm

def clients(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'client/new_client.html', context)
        else:
            return render(request, 'client/new_client.html', context)
    else:
        form = ClientRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,"client/new_client.html",context)

    
