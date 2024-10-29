from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import BypassForm
from .models import Statie, Client, Particular, Depozit, Test

@login_required
def bypass(request):
    if request.method == 'POST':
        form = BypassForm(request.POST, user=request.user)
        if form.is_valid():
            bypass = form.save(commit=False)
            bypass.utilizator = request.user

            # Populare automată a câmpurilor cod_statie și info_statie
            tip_statie = request.POST.get('tip_statie')
            statie_id = request.POST.get('nume_statie')

            if tip_statie and statie_id:
                if tip_statie == 'Statie':
                    statie = get_object_or_404(Statie, id=statie_id)
                elif tip_statie == 'Client':
                    statie = get_object_or_404(Client, id=statie_id)
                elif tip_statie == 'Particular':
                    statie = get_object_or_404(Particular, id=statie_id)
                elif tip_statie == 'Depozit':
                    statie = get_object_or_404(Depozit, id=statie_id)
                elif tip_statie == 'Test':
                    statie = get_object_or_404(Test, id=statie_id)

                bypass.cod_statie = statie.cod_statie
                bypass.info_statie = statie.info_statie

            bypass.save()
            return redirect('formular_bypass')
    else:
        form = BypassForm(user=request.user)

    return render(request, 'formular_bypass.html', {'form': form})


def get_stations(request, tip_statie):
    try:
        if tip_statie == 'Statie':
            stations = Statie.objects.all()
        elif tip_statie == 'Client':
            stations = Client.objects.all()
        elif tip_statie == 'Particular':
            stations = Particular.objects.all()
        elif tip_statie == 'Depozit':
            stations = Depozit.objects.all()
        elif tip_statie == 'Test':
            stations = Test.objects.all()
        else:
            return JsonResponse({'error': 'Tip de stație necunoscut'}, status=400)

        data = [{'id': station.id, 'nume': station.nume} for station in stations]
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_station_details(request, tip_statie, statie_id):
    try:
        if tip_statie == 'Statie':
            statie = Statie.objects.get(id=statie_id)
        elif tip_statie == 'Client':
            statie = Client.objects.get(id=statie_id)
        elif tip_statie == 'Particular':
            statie = Particular.objects.get(id=statie_id)
        elif tip_statie == 'Depozit':
            statie = Depozit.objects.get(id=statie_id)
        elif tip_statie == 'Test':
            statie = Test.objects.get(id=statie_id)
        else:
            return JsonResponse({'error': 'Tip de stație necunoscut'}, status=400)

        data = {
            'cod_statie': statie.cod_statie,
            'info_statie': statie.info_statie
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
