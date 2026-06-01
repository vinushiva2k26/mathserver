# Ex.04 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage, using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```

views.py
from django.shortcuts import render

def bill(request):

    total = None

    if request.method == "POST":

        price = float(request.POST['price'])
        gst = float(request.POST['gst'])

        total = price + (price * gst / 100)

    return render(request, "mathapp/math.html", {"total": total})

mathapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bill, name='bill'),
]

test4/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mathapp.urls')),
]

math.html

<!DOCTYPE html>
<html>
<head>

<title>GST Bill Calculator</title>

<style>

body{
    font-family:Arial;
    background:#f2f2f2;
}

.container{
    width:400px;
    margin:100px auto;
    background:white;
    padding:30px;
    border-radius:10px;
    text-align:center;
    box-shadow:0 0 10px gray;
}

input{
    width:90%;
    padding:10px;
    margin:10px;
}

button{
    padding:10px 20px;
    background:green;
    color:white;
    border:none;
}

.result{
    color:red;
    font-size:24px;
    margin-top:20px;
}

</style>

</head>

<body>

<div class="container">

<h1>GST Bill Calculator</h1>

<form method="post">
    {% csrf_token %}

    <input type="number" name="price" placeholder="Enter Price" required>

    <input type="number" name="gst" placeholder="Enter GST %" required>

    <button type="submit">Calculate Bill</button>
</form>

{% if total %}

<div class="result">
Total Bill Amount = ₹ {{ total }}
</div>

{% endif %}

</div>

</body>
</html>

```

## OUTPUT - SERVER SIDE:

![Output](<Screenshot 2026-06-01 103758.png>)

## OUTPUT - WEBPAGE:

![Output](<Screenshot 2026-06-01 103408.png>)

![Output](<Screenshot 2026-06-01 103422.png>)


## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
