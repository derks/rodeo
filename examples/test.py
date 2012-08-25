
import rodeo

data = dict()
data['people'] = [
    dict(first_name='John', last_name='Doe'),
    dict(first_name='Rita', last_name='Sampson'),
    ]
print rodeo.render_file('examples/test.rodeo', data)
