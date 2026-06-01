from django.shortcuts import render

def bill(request):

    total = None

    if request.method == "POST":

        price = float(request.POST['price'])
        gst = float(request.POST['gst'])

        total = price + (price * gst / 100)

    return render(request, "mathapp/math.html", {"total": total})