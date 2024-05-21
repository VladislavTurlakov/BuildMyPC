from django.contrib import admin
from .models import OS, SSD, CPUCooler, Case, CPU, GPU, MotherBoard, RAM, PowerSupply

# Register your models here.
admin.site.site_header = "Программа по подбору комплектующих ПК"
admin.site.site_title = "Административный сайт"
admin.site.index_title = "Подбор комплектующих ПК"

admin.site.register(OS)
admin.site.register(SSD)
admin.site.register(CPUCooler)
admin.site.register(Case)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(MotherBoard)
admin.site.register(RAM)
admin.site.register(PowerSupply)
