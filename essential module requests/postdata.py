import requests

my_data = {'name':'Nick', 'email':'email@example.com'} 
r = requests.post('https://tryphp.w3schools.com/showphp.php?filename=demo_form_post', data = my_data)

print('Status:', r.status_code)

print(r.url)

f = open('myfile.html','w+')
f.write(r.text)