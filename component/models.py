from django.db import models

# Create your models here.
class OS(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    mode = models.IntegerField()
    maxSupportedMemory = models.IntegerField()
    class Meta:
        verbose_name = 'ОС'
        verbose_name_plural = 'ОС'

    def __str__(self):
        return self.name

class SSD(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    formFactor = models.CharField(max_length=100)
    cache = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'SSD'
        verbose_name_plural = 'SSD'

    def __str__(self):
        return self.name

class CPUCooler(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    fanRPM = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    noiseLevel = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        verbose_name = 'Кулер'
        verbose_name_plural = 'Кулеры'

    def __str__(self):
        return self.name
    
class Case(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    sidePanel = models.CharField(max_length=100)
    externalBays = models.IntegerField()
    class Meta:
        verbose_name = 'Системный блок'
        verbose_name_plural = 'Системные блоки'

    def __str__(self):
        return self.name

class CPU(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    coreCount = models.IntegerField()
    boostClock = models.DecimalField(max_digits=6, decimal_places=2)
    integratedGraphics = models.CharField(max_length=100)
    coreClock = models.FloatField()
    TDP = models.IntegerField()
    class Meta:
        verbose_name = 'Центральный процессор'
        verbose_name_plural = 'Ценральные процессоры'

    def __str__(self):
        return self.name

class GPU(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    chipSet = models.CharField(max_length=100)
    coreClock = models.FloatField()
    color = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    boostClock = models.FloatField()
    length = models.IntegerField()
    class Meta:
        verbose_name = 'Графический процессор'
        verbose_name_plural = 'Графические процессоры'

    def __str__(self):
        return self.name
    
class MotherBoard(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    socket = models.CharField(max_length=100)
    memoryMax = models.IntegerField()
    formFactor = models.CharField(max_length=100)
    memorySlots = models.IntegerField()
    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'

    def __str__(self):
        return self.name

class RAM(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    modules = models.CharField(max_length=100)
    CASLatency = models.IntegerField()
    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'

    def __str__(self):
        return self.name
    
class PowerSupply(models.Model):
    cost = models.FloatField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    wattage = models.IntegerField()
    efficiencyRating = models.CharField(max_length=100)
    modular = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'

    def __str__(self):
        return self.name