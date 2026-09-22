from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def bahubali(request):
    return render(request, "movie.html", {
        "title": "Baahubali",
        "hero": "Prabhas",
        "genre": "Action / Drama",
        "language": "Telugu",
    })


def pushpa(request):
    return render(request, "movie.html", {
        "title": "Pushpa",
        "hero": "Allu Arjun",
        "genre": "Action / Drama",
        "language": "Telugu",
    })


def rrr(request):
    return render(request, "movie.html", {
        "title": "RRR",
        "hero": "Jr. NTR and Ram Charan",
        "genre": "Action / Drama",
        "language": "Telugu",
    })


def salaar(request):
    return render(request, "movie.html", {
        "title": "Salaar",
        "hero": "Prabhas",
        "genre": "Action / Thriller",
        "language": "Telugu",
    })


def kgf(request):
    return render(request, "movie.html", {
        "title": "KGF",
        "hero": "Yash",
        "genre": "Action / Drama",
        "language": "Kannada",
    })


def vikram(request):
    return render(request, "movie.html", {
        "title": "Vikram",
        "hero": "Kamal Haasan",
        "genre": "Action / Thriller",
        "language": "Tamil",
    })


def leo(request):
    return render(request, "movie.html", {
        "title": "Leo",
        "hero": "Vijay",
        "genre": "Action / Thriller",
        "language": "Tamil",
    })


def jailer(request):
    return render(request, "movie.html", {
        "title": "Jailer",
        "hero": "Rajinikanth",
        "genre": "Action / Comedy",
        "language": "Tamil",
    })


def devara(request):
    return render(request, "movie.html", {
        "title": "Devara",
        "hero": "Jr. NTR",
        "genre": "Action / Drama",
        "language": "Telugu",
    })


def kalki(request):
    return render(request, "movie.html", {
        "title": "Kalki 2898 AD",
        "hero": "Prabhas",
        "genre": "Science Fiction / Action",
        "language": "Telugu",
    })