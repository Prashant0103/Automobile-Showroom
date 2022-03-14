from auto.forms import cform

def Search():
    form = cform()
    if form.is_valid:
        name = form.cleaned_data['name']
        print(name)
        
    else:
        print('error')
        
Search()