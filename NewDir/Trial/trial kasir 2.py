import re  # Mengimpor modul regex


class Product:
    def __init__(self, product_code, name, price, stock_quantity):
        self.product_code = product_code
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def display_product_info(self):
        """Menampilkan informasi produk (kode, nama, harga, stok)"""
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
        self.total_price = 0  # Total harga tanpa diskon
        self.discount = 0  # Persentase diskon
        self.payment = 0  # Jumlah pembayaran
        self.change = 0  # Kembalian

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
        if discount_percentage < 0 or discount_percentage > 100:
            print("Diskon tidak valid. Harus antara 0% hingga 100%.")
        else:
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

        # Memastikan kode produk unik dan sesuai format "P" diikuti 3 digit angka
        while True:
            product_code = input("Masukkan kode produk (contoh: P001, P123): ")
            if not re.match(r'^P\d{3}$', product_code):
                print(
                    "Kode produk tidak valid. Kode harus dimulai dengan 'P' diikuti dengan 3 digit angka (misal: P001).")
            elif any(product.product_code == product_code for product in products):
                print(f"Kode produk {product_code} sudah ada. Silakan masukkan kode produk lain.")
            else:
                break

        # Memastikan nama produk dimasukkan sebelum harga
        name = input("Masukkan nama produk: ")
        while not name:
            print("Nama produk tidak boleh kosong.")
            name = input("Masukkan nama produk: ")

        # Memastikan harga dimasukkan sebelum stok
        while True:
            try:
                price = float(input("Masukkan harga produk: "))
                if price < 0:
                    print("Harga tidak boleh negatif.")
                    continue
                break
            except ValueError:
                print("Harga harus berupa angka.")

        # Memastikan jumlah stok dimasukkan
        while True:
            try:
                stock_quantity = int(input("Masukkan jumlah stok produk: "))
                if stock_quantity < 0:
                    print("Stok tidak boleh negatif.")
                    continue
                break
            except ValueError:
                print("Jumlah stok harus berupa angka.")

        # Setelah semua input valid, menambahkan produk ke daftar
        new_product = Product(product_code, name, price, stock_quantity)
        products.append(new_product)

        # Menanyakan apakah admin ingin menambah produk lagi
        another = input("\nIngin menambah produk lagi? (y/n): ").lower()
        if another != 'y':
            break

    return products


def main_menu():
    """Menu utama untuk memilih opsi"""
    print("Selamat datang di Program Kasir!")
    products = []  # Daftar produk kosong pada awalnya

    while True:
        print("\nMenu:")
        print("1. Admin input produk")
        print("2. Pembelian oleh pelanggan")
        print("3. Keluar")

        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            # Admin menginput produk
            products = admin_input_products()
            print("\nProduk berhasil ditambahkan. Kembali ke menu utama.")
        elif choice == '2':
            # Memastikan hanya produk yang ditambahkan admin yang bisa dibeli
            if not products:
                print("\nTidak ada produk yang tersedia untuk dibeli. Admin harus menambahkan produk terlebih dahulu.")
                continue

            print("\nDaftar Produk yang Tersedia untuk Dibeli:")
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
                    while True:
                        try:
                            quantity = int(input(f"Masukkan jumlah {product.name} yang ingin dibeli: "))
                            if quantity <= 0:
                                print("Jumlah pembelian harus lebih besar dari 0.")
                                continue
                            break
                        except ValueError:
                            print("Jumlah produk harus berupa angka.")
                    transaction.add_product(product, quantity)
                else:
                    print("Produk tidak ditemukan, coba lagi.")

            # Opsi diskon
            discount_code = input("\nApakah Anda memiliki kode diskon? (y/n): ").lower()
            if discount_code == 'y':
                while True:
                    try:
                        discount_percentage = float(input("Masukkan persentase diskon: "))
                        transaction.apply_discount(discount_percentage)
                        break
                    except ValueError:
                        print("Diskon harus berupa angka.")

            # Menghitung total harga
            transaction.calculate_total()

            # Menampilkan total harga dan meminta pembayaran
            print(f"\nTotal yang harus dibayar: {transaction.total_price}")
            while True:
                try:
                    payment = float(input("Masukkan jumlah pembayaran: "))
                    if payment < transaction.total_price:
                        print("Uang yang dimasukkan kurang. Silakan masukkan jumlah yang cukup.")
                        continue  # Jika uang kurang, ulangi input
                    break
                except ValueError:
                    print("Jumlah pembayaran harus berupa angka.")

            if transaction.process_payment(payment):
                # Menampilkan struk dan kembalian
                transaction.generate_receipt()
            else:
                print("Pembayaran tidak cukup, coba lagi.")

        elif choice == '3':
            print("Terima kasih telah menggunakan program kasir!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


# Menjalankan menu utama
main_menu()
