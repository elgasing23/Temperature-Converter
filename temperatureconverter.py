def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    print("Selamat datang di Konverter Suhu!")

    while True:
        suhu = input("Masukkan suhu (atau ketik 'keluar' untuk berhenti): ")
        if suhu.lower() == 'keluar':
            print("Terima kasih telah menggunakan program ini. Selamat tinggal!")
            break
        
        try:
            suhu = float(suhu)
        except ValueError:
            print("Silakan masukkan angka yang valid.")
            continue
        
        satuan = input("Masukkan satuan suhu (C untuk Celsius, F untuk Fahrenheit, K untuk Kelvin): ").upper()

        if satuan == 'C':
            print(f"{suhu} °C = {celsius_to_fahrenheit(suhu):.2f} °F")
            print(f"{suhu} °C = {celsius_to_kelvin(suhu):.2f} K")
        elif satuan == 'F':
            print(f"{suhu} °F = {fahrenheit_to_celsius(suhu):.2f} °C")
            print(f"{suhu} °F = {fahrenheit_to_kelvin(suhu):.2f} K")
        elif satuan == 'K':
            print(f"{suhu} K = {kelvin_to_celsius(suhu):.2f} °C")
            print(f"{suhu} K = {kelvin_to_fahrenheit(suhu):.2f} °F")
        else:
            print("Satuan tidak valid. Silakan masukkan C, F, atau K.")

if __name__ == "__main__":
    main()
