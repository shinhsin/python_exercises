import twder

dollar = twder.now_all()

print("Date:", dollar['USD'][0])

print("{:9s}\t{:9s}\t{:9s}\t{:9s}\t{:9s}".
      format('Currency', 'Cash_Buy', 'Cash_Sell', 'Rate_Buy', 'Rate_Sell'))

for currency in dollar.keys():
    print(f"{currency:9s}\t", end='')
    for cnt in range(1, len(dollar[currency])):
        if '-' != dollar[currency][cnt]:
            print(f" {dollar[currency][cnt].zfill(5):8s}\t", end='')
        else:
            print("{:9s}".format(' -'), "\t", end='')
    print("")
