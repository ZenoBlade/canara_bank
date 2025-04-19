from django.shortcuts import render, redirect,HttpResponse
from .models import bank
# Create your views here.
def home(request):
    return render (request,'home.html')

# ------------------ ACC CREATION ------------------
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        aadhar = request.POST.get('aadhar')
        email = request.POST.get('email')
        address = request.POST.get('address')
        bank.objects.create(name=name,gender=gender,phone=phone,aadhar=aadhar,email=email,address=address,)
        return redirect('home')
    

    return render(request, 'create.html')

# ------------------ PIN GENERATION ------------------
def pingen(request):
    if request.method == "POST":
        acc_num = request.POST.get("acc_num")
        pin = request.POST.get("pin")
        confirm_pin = request.POST.get("confirm_pin")

        acc = bank.objects.filter(acc_num=acc_num).first()

        if acc:
            if pin == confirm_pin:
                acc.pin = pin
                acc.save()
                print("PIN set successfully.")
            else:
                print("PINs do not match.")
        else:
            print("Account not found.")

    return render(request, "pin.html")


# ------------------ DEPOSIT ------------------
def deposit(request):
    if request.method == "POST":
        acc_num = request.POST.get("acc_num")
        amount = request.POST.get("amount")
        pin = request.POST.get("pin")
        
        if acc_num and amount and pin and pin.isdigit() and amount.isdigit():
            pin=int(pin)
            amount = int(amount)
            acc = bank.objects.get(acc_num=acc_num)
            if acc.pin == pin:
                acc.balance += amount
                acc.save()
                print(f"₹{amount} deposited. New balance: ₹{acc.balance}")
            else:
                print("Account not found.")
        else:
            print("Invalid input.")

    return render(request, "deposit.html")


# ------------------ WITHDRAWAL ------------------
def withdraw(request):
    if request.method == "POST":
        acc_num = request.POST.get("acc_num")
        amount = request.POST.get("amount")
        pin = request.POST.get("pin")
        
        if acc_num and amount and pin and pin.isdigit() and amount.isdigit():
            pin = int(pin)
            amount = int(amount)
            acc = bank.objects.get(acc_num=acc_num)
            if acc.pin == pin:
                if acc.balance >= amount:
                    acc.balance -= amount
                    acc.save()
                    print(f"₹{amount} withdrawn. New balance: ₹{acc.balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid PIN.")
        else:
            print("Invalid input.")

    return render(request, "withdraw.html")

# ------------------ BALANCE CHECK ------------------
def balance(request):
    if request.method == "POST":
        acc_num = request.POST.get("acc_num")
        pin = request.POST.get("pin")
        
        if acc_num and pin and pin.isdigit():
            pin = int(pin)
            acc = bank.objects.get(acc_num=acc_num)
            if acc.pin == pin:
                print(f"Account balance: ₹{acc.balance}")
            else:
                print("Invalid PIN.")
        else:
            print("Invalid input.")
    
    return render(request, "bal.html")


# ------------------ ACCOUNT TRANSFER ------------------
def acctransfer(request):
    if request.method == "POST":
        from_acc_num = request.POST.get("from_acc_num")
        to_acc_num = request.POST.get("to_acc_num")
        amount = request.POST.get("amount")
        pin = request.POST.get("pin")
        
        if from_acc_num and to_acc_num and amount and pin and pin.isdigit() and amount.isdigit():
            pin = int(pin)
            amount = int(amount)
            
            # Get the source account
            from_acc = bank.objects.get(acc_num=from_acc_num)
            
            # Get the destination account
            to_acc = bank.objects.get(acc_num=to_acc_num)
            
            if from_acc.pin == pin:
                if from_acc.balance >= amount:
                    # Perform the transfer
                    from_acc.balance -= amount
                    to_acc.balance += amount
                    from_acc.save()
                    to_acc.save()
                    print(f"₹{amount} transferred from {from_acc_num} to {to_acc_num}. New balance: ₹{from_acc.balance} (Source Account), ₹{to_acc.balance} (Destination Account).")
                else:
                    print("Insufficient balance in the source account.")
            else:
                print("Invalid PIN.")
        else:
            print("Invalid input.")
    
    return render(request, "transfer.html")

