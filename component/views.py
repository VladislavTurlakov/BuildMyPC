from django.shortcuts import render
from .models import OS, SSD, CPUCooler, Case, CPU, GPU, MotherBoard, RAM, PowerSupply 

# Create your views here.
def hello_world(request):
    return render(request, 'index.html', {'greeting': 'Hello, world!'})

def os(request):
    os = OS.objects.all()
    context = {
        'os': os
    }
    return render(request, 'os.html', context)

def ssd(request):
    ssd = SSD.objects.all()
    context = {
        'ssd': ssd
    }
    return render(request, 'ssd.html', context)

def cpucooler(request):
    cpucooler = CPUCooler.objects.all()
    context = {
        'cpucooler': cpucooler
    }
    return render(request, 'cpucooler.html', context)

def case(request):
    case = Case.objects.all()
    context = {
        'case': case
    }
    return render(request, 'case.html', context)

def cpu(request):
    cpu = CPU.objects.all()
    context = {
        'cpu': cpu
    }
    return render(request, 'cpu.html', context)

def gpu(request):
    gpu = GPU.objects.all()
    context = {
        'gpu': gpu
    }
    return render(request, 'gpu.html', context)

def motherboard(request):
    motherboard = MotherBoard.objects.all()
    context = {
        'motherboard': motherboard
    }
    return render(request, 'motherboard.html', context)

def ram(request):
    ram = RAM.objects.all()
    context = {
        'ram': ram
    }
    return render(request, 'ram.html', context)

def powersupply(request):
    powersupply = PowerSupply.objects.all()
    context = {
        'powersupply': powersupply
    }
    return render(request, 'powersupply.html', context)