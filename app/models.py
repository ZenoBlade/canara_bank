from django.db import models
# Create your models here.
class bank(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    phone = models.IntegerField()
    aadhar = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=150)
    acc_num = models.BigIntegerField(unique=True)
    pin = models.IntegerField(default=0)
    balance = models.DecimalField(decimal_places=2,default=1000,max_digits=7)
    address = models.TextField()

    def save(self,*args, **kwargs):
        if not self.acc_num:
            last_account=bank.objects.order_by('-acc_num').first()
            if last_account:
                self.acc_num = last_account.acc_num + 1 
            else:
                self.acc_num=1234567890
        super().save(*args, **kwargs)