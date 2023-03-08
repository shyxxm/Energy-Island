from django.db import models

# Create your models here.
class Households (models.Model):
    HouseholdID = models.AutoField(primary_key=True)
    Address = models.CharField(max_length=100, null = True)
    NumOccupants = models.IntegerField(null = True)
    TotalSqFt = models.DecimalField(max_digits=8, decimal_places=2, null = True)
    NumRooms = models.IntegerField(null = True)


class ApplianceTypes (models.Model):
    ApplianceTypeID = models.AutoField(primary_key=True)
    ApplianceTypeName = models.CharField(max_length=100, null = True)
    EnergyConsumptionRate = models.DecimalField(max_digits=8, decimal_places=2, null = True)

class Appliances (models.Model):
    ApplianceID = models.AutoField(primary_key=True)
    ApplianceName = models.CharField(max_length=100,null = True)
    ApplianceTypeID = models.ForeignKey(ApplianceTypes, on_delete = models.CASCADE)
    HouseholdID = models.ForeignKey(Households, on_delete = models.CASCADE) 

class EnergyUsage (models.Model):
    EnergyUsageID = models.AutoField(primary_key=True)
    UsageDatetime = models.DateTimeField(null = True)
    EnergyConsumed = models.DecimalField(max_digits=8, decimal_places=2, null = True)
    ApplianceID = models.ForeignKey(Appliances, on_delete = models.CASCADE)

class EnergyRates (models.Model):
    RateID = models.AutoField(primary_key=True)
    StartDatetime = models.DateTimeField(null = True)
    EndDatetime = models.DateTimeField(null = True)
    EnergyRate = models.DecimalField(max_digits=8, decimal_places=2, null = True)

class Billing (models.Model):
    BillingID = models.AutoField(primary_key=True)
    HouseholdID = models.ForeignKey(Households, on_delete=models.CASCADE)
    StartDateime = models.DateTimeField(null = True)
    EndDatetime = models.DateTimeField(null = True)
    TotalEnergyConsumed = models.DecimalField(max_digits=8, decimal_places=2, null = True)
    EnergyRateID = models.ForeignKey(EnergyRates, on_delete=models.CASCADE)
    TotalCost = models.DecimalField(max_digits=10, decimal_places=2, null = True)
