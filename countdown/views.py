from django.shortcuts import render, redirect

from .forms import DOBForm


def home(request):
    dob_form = DOBForm(request.POST or None)
    if request.method == 'POST':
        if dob_form.is_valid():
            dob = dob_form.cleaned_data['dob'].date()
            return redirect(f'grid/{dob}')
    return render(request, 'home.html', {'dob_form': dob_form})


def grid(request, dob):
    if not DOBForm(data={'dob': dob}).is_valid():
        return redirect('/')
    dob_form = DOBForm(data={'dob': dob})
    current_year = dob_form.get_current_year_of_life()
    return render(request, 'grid.html', {
        'years_passed': range(1, current_year),
        'current_year': current_year,
        'future_years': range(current_year + 1, 91),
        'full_year_weeks': range(1, 53),
        'weeks_passed_this_yr': range(1, dob_form.get_current_week_no()),
        'current_week': dob_form.get_current_week_no(),
        'weeks_left_this_yr': range(dob_form.get_current_week_no() + 1, 53)
    })
