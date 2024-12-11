class Product:
    def __init__(self, product_code, name, price, stock_quantity):
        self.product_code = product_code
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def display_product_info(self):
        """Menampilkan informasi produk (kode, nama, harga)"""
        print(f"Kode: {self.product_code} | Nama: {self.name} | Harga: {self.price} | Stok: {self.stock_quantity}")

    def update_stock(self, quantity):
        """Mengurangi stok berdasarkan jumlah yang dibeli"""
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            return True
        return False


class Transaction:
    def __init__(self):
        self.product_list = []  # Daftar produk yang dibeli
        self.total_price = 0    # Total harga tanpa diskon
        self.discount = 0       # Persentase diskon
        self.payment = 0        # Jumlah pembayaran
        self.change = 0         # Kembalian

    def add_product(self, product, quantity):
        """Menambahkan produk ke dalam transaksi"""
        if product.update_stock(quantity):
            self.product_list.append({'product': product, 'quantity': quantity, 'subtotal': product.price * quantity})
            print(f"Ditambahkan ke keranjang: {product.name} x{quantity} - {product.price * quantity}")
        else:
            print(f"Stok tidak cukup untuk produk {product.name}")

    def calculate_total(self):
        """Menghitung total harga transaksi"""
        self.total_price = sum(item['subtotal'] for item in self.product_list)
        if self.discount > 0:
            self.total_price -= self.total_price * (self.discount / 100)

    def apply_discount(self, discount_percentage):
        """Menerapkan diskon pada total harga"""
        self.discount = discount_percentage
        print(f"Diskon {self.discount}% diterapkan.")

    def process_payment(self, payment_amount):
        """Memproses pembayaran dan menghitung kembalian"""
        self.payment = payment_amount
        if self.payment >= self.total_price:
            self.change = self.payment - self.total_price
            return True
        return False

    def generate_receipt(self):
        """Mencetak struk pembelian"""
        print("\n--- Struk Pembelian ---")
        for item in self.product_list:
            print(f"{item['product'].name} x{item['quantity']} = {item['subtotal']}")
        print(f"Total: {self.total_price}")
        if self.discount > 0:
            print(f"Diskon: {self.discount}%")
        print(f"Total setelah diskon: {self.total_price}")
        print(f"Pembayaran: {self.payment}")
        print(f"Kembalian: {self.change}")
        print("\nTerima kasih telah berbelanja!")


def admin_input_products():
    """Fungsi untuk menginput daftar produk oleh admin"""
    products = []
    while True:
        print("\n--- Input Produk Baru ---")
        product_code = input("Masukkan kode produk: ")
        name = input("Masukkan nama produk: ")
        price = float(input("Masukkan harga produk: "))
        stock_quantity = int(input("Masukkan jumlah stok produk: "))

        new_product = Product(product_code, name, price, stock_quantity)
        products.append(new_product)

        another = input("\nIngin menambah produk lagi? (y/n): ").lower()
        if another != 'y':
            break

    return products


# Mulai program
print("Selamat datang di Program Kasir!")
print("1. Admin input produk")
print("2. Pembelian oleh pelanggan")

choice = input("Pilih opsi: ")

if choice == '1':
    # Admin menginput produk
    products = admin_input_products()
elif choice == '2':
    # Misalnya, kita memiliki beberapa produk yang sudah tersedia
    products = [
        Product("P001", "Laptop", 10000000, 5),
        Product("P002", "Smartphone", 5000000, 10),
        Product("P003", "Headphone", 500000, 20),
        Product("P004", "Mouse", 150000, 15)
    ]
else:
    print("Pilihan tidak valid!")
    exit()

# Menampilkan produk yang tersedia
print("\nDaftar Produk:")
for product in products:
    product.display_product_info()

# Membuat transaksi baru
transaction = Transaction()

while True:
    # Memilih produk
    product_code = input("\nMasukkan kode produk (atau 'exit' untuk selesai): ")
    if product_code.lower() == 'exit':
        break

    # Mencari produk berdasarkan kode
    product = next((p for p in products if p.product_code == product_code), None)

    if product:
        quantity = int(input(f"Masukkan jumlah {product.name} yang ingin dibeli: "))
        transaction.add_product(product, quantity)
    else:
        print("Produk tidak ditemukan, coba lagi.")

# Opsi diskon
discount_code = input("\nApakah Anda memiliki kode diskon? (y/n): ").lower()
if discount_code == 'y':
    discount_percentage = float(input("Masukkan persentase diskon: "))
    transaction.apply_discount(discount_percentage)

# Menghitung total harga
transaction.calculate_total()

# Menampilkan total harga dan meminta pembayaran
print(f"\nTotal yang harus dibayar: {transaction.total_price}")
payment = float(input("Masukkan jumlah pembayaran: "))

if transaction.process_payment(payment):
    # Menampilkan struk dan kembalian
    transaction.generate_receipt()
else:
    print("Pembayaran tidak cukup, coba lagi.")

