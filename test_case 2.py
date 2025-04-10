from tabulate import tabulate

# Plan order untuk validasi
plan_order = {"Basic Plan": 1, "Standard Plan": 2, "Premium Plan": 3}

# Simulasi data user
data = {
    "shandy": ["Basic Plan", 12, "shandy-2134"],
    "cahya": ["Standard Plan", 24, "cahya-abcd"],
    "ana": ["Premium Plan", 5, "ana-2f9g"],
    "bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class User:
    def __init__(self, username):
        self.username = username
        if username in data:
            self.current_plan = data[username][0]
            self.duration_plan = data[username][1]
        else:
            raise Exception("User tidak ditemukan.")

    def check_benefit(self):
        table = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]
        headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]
        print("\nPacFlix Plan List\n")
        print(tabulate(table, headers))

    def check_plan(self):
        value = data[self.username]
        print(f"\nPlan Anda: {value[0]}")
        print(f"Durasi Berlangganan: {value[1]} bulan\n")

    def upgrade_plan(self, new_plan):
        if plan_order[new_plan] <= plan_order[self.current_plan]:
            return "Tidak bisa downgrade atau tetap di plan yang sama."

        if self.duration_plan > 12:
            diskon = 0.05
        else:
            diskon = 0.0

        harga_plan = {"Basic Plan": 120_000, "Standard Plan": 160_000, "Premium Plan": 200_000}
        total = harga_plan[new_plan] * (1 - diskon)
        data[self.username][0] = new_plan  # update plan
        return f"Upgrade berhasil. Total biaya setelah diskon: Rp {int(total)}"

class NewUser:
    def __init__(self, username):
        self.username = username
        self.check_list = [val[2] for val in data.values()]

    def daftar(self, plan, referral_code):
        if referral_code not in self.check_list:
            return "Referral tidak valid."

        harga_plan = {"Basic Plan": 120_000, "Standard Plan": 160_000, "Premium Plan": 200_000}
        if plan not in harga_plan:
            return "Plan tidak valid."

        total = harga_plan[plan] * 0.96  # diskon 4%
        data[self.username] = [plan, 1, f"{self.username}-ref"]
        return f"Berhasil daftar. Total biaya setelah diskon referral: Rp {int(total)}"

class PacflixApp:
    def run(self):
        while True:
            print("\n--- PACFLIX CLI ---")
            username = input("Masukkan username (atau ketik 'exit' untuk keluar): ").strip().lower()
            if username == "exit":
                print("Terima kasih telah menggunakan PacFlix!")
                break

            print("\n1. Lihat semua plan")
            print("2. Cek plan saya")
            print("3. Upgrade plan")
            print("4. Daftar user baru (pakai referral)")
            print("5. Ganti user")

            pilihan = input("Pilih menu: ")

            try:
                if pilihan == "1":
                    User(username).check_benefit()

                elif pilihan == "2":
                    User(username).check_plan()

                elif pilihan == "3":
                    new_plan = input("Masukkan plan baru: ").strip()
                    print(User(username).upgrade_plan(new_plan))

                elif pilihan == "4":
                    plan = input("Masukkan plan: ").strip()
                    referral = input("Masukkan referral code: ").strip()
                    print(NewUser(username).daftar(plan, referral))

                elif pilihan == "5":
                    continue
                else:
                    print("Pilihan tidak valid.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    app = PacflixApp()
    app.run()