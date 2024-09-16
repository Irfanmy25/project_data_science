import getpass

# Data user_id yang valid
valid_users = {
    '031T': '891000',
    '121T': '123456',
    '032T': '010101'
}
# Data awal
loans = [
    {
        'ApplicationID': 101,
        'AccountNumber': 7111897755,
        'Name': 'Agus Santoso',
        'PhoneNumber': 62878717178,
        'CreditScore': 750,
        'LoanAmountRequested': 70000000.00,
        'RiskLevel': 'Low',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 102,
        'AccountNumber': 8121987567,
        'Name': 'Indah Lestari',
        'PhoneNumber': 62896518717,
        'CreditScore': 680,
        'LoanAmountRequested': 90000000.00,
        'RiskLevel': 'Medium',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 103,
        'AccountNumber': 7212199776,
        'Name': 'Boby Pangestu',
        'PhoneNumber': 62856947823,
        'CreditScore': 720,
        'LoanAmountRequested': 65000000.00,
        'RiskLevel': 'Medium',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 104,
        'AccountNumber': 9222199669,
        'Name': 'Restu Anindita',
        'PhoneNumber': 62877948732,
        'CreditScore': 600,
        'LoanAmountRequested': 40000000.00,
        'RiskLevel': 'High',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 105,
        'AccountNumber': 9123170671,
        'Name': 'Bima Soeparno',
        'PhoneNumber': 62812879613,
        'CreditScore': 710,
        'LoanAmountRequested': 50000000.00,
        'RiskLevel': 'Medium',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 106,
        'AccountNumber': 1245678912,
        'Name': 'Bryan James',
        'PhoneNumber': 62812125456,
        'CreditScore': 760,
        'LoanAmountRequested': 250000000.00,
        'RiskLevel': 'Low',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 107,
        'AccountNumber': 7119234411,
        'Name': 'Hasan Suparno',
        'PhoneNumber': 62878163071,
        'CreditScore': 520,
        'LoanAmountRequested': 30000000.00,
        'RiskLevel': 'High',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 108,
        'AccountNumber': 6523561255,
        'Name': 'Lisnawati',
        'PhoneNumber': 62813569485,
        'CreditScore': 650,
        'LoanAmountRequested': 65000000.00,
        'RiskLevel': 'Medium',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 109,
        'AccountNumber': 7564889923,
        'Name': 'Endang Utami',
        'PhoneNumber': 62812879613,
        'CreditScore': 780,
        'LoanAmountRequested': 650000000.00,
        'RiskLevel': 'Low',
        'UserID' : 'SYSTEM'
    },
    {
        'ApplicationID': 110,
        'AccountNumber': 4523556612,
        'Name': 'Akbar Alkatiri',
        'PhoneNumber': 62856658265,
        'CreditScore': 550,
        'LoanAmountRequested': 120000000.00,
        'RiskLevel': 'High',
        'UserID' : 'SYSTEM'
    }
]

# Function login
def login():
    print("===== Bank Central Amanah =====")
    print("\n\tRestricted Area\n")

    # Looping untuk login berkali-kali
    while True :
        user_id = input("User ID\t\t: ").upper()
        password = getpass.getpass(("Password\t: "))  # getpass digunakan untuk tidak menampilkan password yang diinput oleh user

        if user_id in valid_users and valid_users[user_id] == password:
            print("Login berhasil!")
            return user_id # Mengembalikan user_id setelah berhasil login
        else:
            print("Mohon maaf, Anda tidak memiliki akses")
            print("\nGunakan User ID yang memiliki Akses Pada Sistem\n")
            retry = input("Apa Ingin mencoba lagi ? (Y/N) : ").upper() # Pilihan untuk mencoba login kembali
            if retry != "Y" :
                return None # Ketika user memilih N, maka program akan keluar

# Function untuk menambah aplikasi pinjaman baru
def create_loan(user_id):
    if loans:
        application_id = loans[-1]['ApplicationID']+1 # Membuat AplicationID secara otomatis dari data tertinggi pada data sebelumnya
    
    # Looping untuk memastikan nomor rekening tidak duplicate
    existing_account_number = {loan['AccountNumber'] for loan in loans}
    while True :
        account_number = input("Masukkan Nomor Rekening Pemohon : ")
        if account_number in existing_account_number :
            print(f"Nomor rekening {account_number} sudah terdaftar dalam sistem. Silahkan masukkan nomor rekening baru (N) atau lakukan update data (U). ")
            choice = input("Apakah anda ingin memasukkan nomor rekening baru (N) atau melakukan update data (U) ? : ").upper()
            if choice == 'N' :
                continue
            elif choice == 'U' :
                update_loan(user_id)
                return
            else :
                print("Pilihan tidak valid. Kembali ke menu utama.")
                return      
        break

    name = input("Masukkan Nama Pemohon: ").title()

    while True :
        phone_number = input("Masukkan Nomor Telepon Pemohon : ")
        if phone_number.isdigit() :
            break
        else :
            print("Nomor Telepon tidak valid. Harap input Nomor Telepon dengan format angka. Silahkan coba lagi.")
    
    while True :
        try :
            credit_score = int(input("Masukkan Skor Kredit: "))
            break
        except ValueError :
            print("Input tidak valid. Input Skor Kredit dengan format angka. Silahkan coba lagi.")

    while True :
        try :
            loan_amount = float(input("Masukkan Jumlah Pinjaman yang Diminta: "))
            break
        except ValueError :
            print("Input tidak valid. Input Jumlah Pinjaman dengan format angka. Silahkan coba lagi.")

    # Risk Level dibuat secara otomatis berdasarkan credit score yang diinput
    if credit_score >= 750 :
        risk_level = 'Low'
    elif 650 <= credit_score < 750 :
        risk_level = 'Medium'
    else :
        risk_level = 'High'

    loan = {
        'ApplicationID': application_id,
        'AccountNumber' : account_number,
        'Name': name,
        'PhoneNumber' : phone_number,
        'CreditScore': credit_score,
        'LoanAmountRequested': loan_amount,
        'RiskLevel': risk_level,
        'UserID' : user_id
    }

    # Menampilkan data yang akan ditambahkan
    print("\nData yang akan ditambahkan:")
    print(f"Application ID\t\t: {loan['ApplicationID']}")
    print(f"Nomor Rekening\t\t: {loan['AccountNumber']}")
    print(f"Nama Pemohon\t\t: {loan['Name']}")
    print(f"Nomor Telepon\t\t: {loan['PhoneNumber']}")
    print(f"Skor Kredit\t\t: {loan['CreditScore']}")
    print(f"Jumlah Pinjaman\t\t: {loan['LoanAmountRequested']:.2f}")
    print(f"Level Risiko\t\t: {loan['RiskLevel']}")
    
    # Konfirmasi 
    confirm = input("\nApakah Anda yakin ingin menambahkan data ini ? (Y/N): ").upper()
    if confirm == 'Y' :
        loans.append(loan)
        print(f"Data pinjaman dengan Application ID {loan['ApplicationID']} berhasil ditambahkan!")
    elif confirm == 'N' :
        print("Data Pinjaman batal disimpan.\nKembali ke menu utama.")
    else :
        print("Tidak valid. Data Pinjaman batal disimpan. Kembali ke menu utama.")

# Function untuk menampilkan semua aplikasi pinjaman dalam bentuk tabel
def read_loans():
    print("\nDaftar Aplikasi Pinjaman")
    print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'UserID':<10}")
    print("="*120)
    for loan in loans:
            print(f"{loan['ApplicationID']:<15} {loan['AccountNumber']:<15} {loan['Name']:<20} {loan['PhoneNumber']:<15} {loan['CreditScore']:<15} {loan['LoanAmountRequested']:<20.2f} {loan['RiskLevel']:<10} {loan['UserID']:<10}")
    
    # Opsi untuk melakukan search by aplication name
    search = input("\nApakah Anda ingin mencari data tertentu ? (Y/N) : ").upper()
    if search == 'Y' :
        search_loan_by_name () # Memanggil function search
    elif search == 'N' :
        print("Kembali ke menu Utama")
    else :
        print("Tidak Valid.\nKembali ke Menu Utama.")

# Function search
def search_loan_by_name() :
    while True :
        search_name = input("Masukkan Nama yang dicari : ").lower()

        found = False
        print(f"\nHasil Pencarian untuk '{search_name}' :")
        print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'UserID':<10}")
        print("="*120)

        # mencari aplikasi yang sesuai dengan nama yang diinput
        for loan_search in loans :
            if search_name in loan_search['Name'].lower() :
                print(f"{loan_search['ApplicationID']:<15} {loan_search['AccountNumber']:<15} {loan_search['Name']:<20} {loan_search['PhoneNumber']:<15} {loan_search['CreditScore']:<15} {loan_search['LoanAmountRequested']:<20.2f} {loan_search['RiskLevel']:<10} {loan_search['UserID']:<10}")
                found = True
            
        if not found:
            print("Nama Applicant tidak ditemukan.")

        # Opsi mencari data lain
        search_angain = input("\nApakah Anda ingin mencari data lain ? (Y/N) : ").upper()
        if search_angain =='Y' :
            continue
        elif search_angain == 'N' :
            print("Kembali ke menu utama")
            break    
        else:
            print("Tidak Valid.\nKembali ke Menu Utama.")
            break # keluar dari loop search data dan kembali ke menu utama

# Function untuk memperbarui data pinjaman berdasarkan ApplicationID
def update_loan(user_id):
    while True :
        try :
            application_id = int(input("Masukkan Application ID yang akan diperbarui: "))
            loan_found = False # Melacak apakah id ditemukan

            for loan in loans:
                if loan['ApplicationID'] == application_id:
                    loan_found = True 
                    print(f"\nData Lama :")
                    print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'UserID':<10}")
                    print("="*120)
                    print(f"{loan['ApplicationID']:<15} {loan['AccountNumber']:<15} {loan['Name']:<20} {loan['PhoneNumber']:<15} {loan['CreditScore']:<15} {loan['LoanAmountRequested']:<20.2f} {loan['RiskLevel']:<10} {loan['UserID']:<10}")
                    
                    # Pilihan Kategori Update Data
                    print("\nPilih Kategori Data yang ingin diupdate :")
                    print("1. Account Number")
                    print("2. Name")
                    print("3. Phone Number")
                    print("4. Credit Score")
                    print("5. Loan Amount Requested")

                    choice = input("Masukkan pilihan (1-5): ")

                    existing_account_number = {loan['AccountNumber'] for loan in loans}

                    # Input berdasarkan kategori update yang user pilih
                    if choice == '1' :
                        updated_data = input("Masukkan Nomor Rekening yang terupdate : ")
                        # Pengecekan jika nomor rekening sudah ada/duplicate
                        if updated_data in existing_account_number and updated_data != str(loan['AccountNumber']) :
                            print(f"Nomor rekening {updated_data} sudah terdaftar dalam sistem.")
                            print("Kembali ke menu utama.")
                            return # Kembali ke menu utama
                        field = 'AccountNumber'
                    elif choice == '2' :
                        updated_data = input("Masukkan Nama Pemohon yang terupdate : ").title()
                        field = 'Name'
                    elif choice == "3" :
                        updated_data = input("Masukkan Nomor Telepon yang terupdate : ")
                        if not updated_data.isdigit() :
                            print("Update Data dibatalkan. Format Nomor Telepon tidak sesuai.")
                            return
                        field = 'PhoneNumber'
                    elif choice == "4" :
                        updated_data = input("Masukkan Skor Kredit yang terupdate : ")
                        # Update RiskLevel berdasarkan rules CreditScore 
                        try :
                            updated_data = int(updated_data)
                            if updated_data >= 750 :
                                loan['RiskLevel'] = 'Low'
                            elif 650 <= updated_data < 750 :
                                loan['RiskLevel'] = 'Medium'
                            else :
                                loan['RiskLevel'] = 'High'
                        except ValueError :
                            print("Update Data dibatalkan. Format Skor Kredit tidak sesuai.")
                            return
                        field = 'CreditScore'
                    elif choice == '5' :
                        updated_data = input("Masukkan Permintaan Jumlah Pinjaman yang terupdate : ")
                        try :
                            updated_data = float(updated_data)
                        except ValueError :
                            print("Update Data dibatalkan, Format Jumlah Pinjaman tidak sesuai.")
                            return
                        field = 'LoanAmountRequested'
                    else : 
                        print("Pilihan Tidak Valid. Kembali ke menu utama.")
                        return
                    
                    # Confirm perubahan data
                    confirm = input(f"Apakah Anda yakin data {field} akan diupdate ? (Y/N) : ").upper()

                    if confirm == 'Y' :
                        if field == 'CreditScore' :
                            loan[field] = int(updated_data)
                        elif field == "LoanAmountRequested" :
                            loan[field] = float(updated_data)
                        else :
                            loan[field] = updated_data

                        loan['UserID'] = user_id # Update user ID
                        print(f"Data {field} berhasil diperbarui!")
                    elif confirm == 'N' :
                        print(f"Update {field} dibatalkan. ")
                    else :
                        print(f"Tidak valid, Update data tidak dapat dilakukan. Kembali ke menu utama")
                    return
            if not loan_found :
                print(f"\nData Lama :")
                print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'UserID':<10}")
                print("="*120)
                print(f"Application ID {application_id} tidak ditemukan.")
                break
        except ValueError :
            print(f"\nData Lama :")
            print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'UserID':<10}")
            print("="*120)
            print("Application ID tidak valid. Harap Masukkan Application ID yang sesuai.")
            return
# Global list untuk menyimpan data yang dihapus
deleted_loans = []

# Function untuk menghapus data pinjaman berdasarkan ApplicationID
def delete_loan(user_id):
    while True :
        try :
            global loans
            application_id = int(input("Masukkan Application ID yang akan dihapus: "))
            
            # Search data yang akan dihapus
            loan_to_delete = None
            for loan in loans :
                if loan['ApplicationID'] == application_id :
                    loan_to_delete = loan
                    break
            
            # Menampilkan data yang telah dicari (Yang akan dihapus)
            if loan_to_delete :
                print(f"\nData yang akan dihapus:")
                print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'UserID':<10}")
                print("="*120)
                print(f"{loan_to_delete['ApplicationID']:<15} {loan_to_delete['AccountNumber']:<15} {loan_to_delete['Name']:<20} {loan_to_delete['PhoneNumber']:<15} {loan_to_delete['CreditScore']:<15} {loan_to_delete['LoanAmountRequested']:<20.2f} {loan_to_delete['RiskLevel']:<10} {loan_to_delete['UserID']:<10}")
            
                # Confirm delete
                confirm = input("\nApakah Anda yakin ingin menghapus data ini ? (Y/N) : ").upper()
                if confirm == 'Y' :
                    # Menambahkan user_id yang melakukan transaksi delete
                    loan_to_delete['DeletedBy'] = user_id
                    deleted_loans.append(loan_to_delete) # Menyimpan data yang telah dihapus

                    loans = [loan for loan in loans if loan['ApplicationID'] != application_id]
                    print(f"Data dengan Application ID {application_id} berhasil dihapus.")
                    break
                elif confirm == 'N' :
                    print("Penghapusan Data dibatalkan.")
                else :
                    print("Tidak valid. Penghapusan Data dibatalkan. Kembali ke menu utama")
                break
            else :
                print(f"\nData yang akan dihapus:")
                print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'UserID':<10}")
                print("="*120)
                print(f"Application ID {application_id} tidak ditemukan.")
                break
        except ValueError :
            print(f"\nData yang akan dihapus:")
            print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'UserID':<10}")
            print("="*120)
            print("Application ID tidak valid. Harap masukkan Application ID yang sesuai.")
            break

# Function untuk melihat data yang telah dihapus
def view_deleted_loans():
    if deleted_loans:
        print("\nData Aplikasi Pinjaman yang Telah Dihapus")
        print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'DeletedBy':<10}")
        print("="*120)
        for loan in deleted_loans :
            print(f"{loan['ApplicationID']:<15} {loan['AccountNumber']:<15} {loan['Name']:<20} {loan['PhoneNumber']:<15} {loan['CreditScore']:<15} {loan['LoanAmountRequested']:<20.2f} {loan['RiskLevel']:<10} {loan['DeletedBy']:<10}")
    else :
        print("\nData Aplikasi Pinjaman yang Telah Dihapus")
        print(f"{'ApplicationID':<15} {'AccountNumber':<15} {'Name':<20} {'PhoneNumber':<15} {'CreditScore':<15} {'LoanAmountRequested':<20} {'RiskLevel':<10} {'DeletedBy':<10}")
        print("="*120)
        print("Tidak ada data yang telah dihapus.")


def main():
    user_id = login() # Menyimpan user_id yang didapatkan ketika login
    
    if user_id is None :
        return
    
    while True:
        print("\nMenu Sistem Manajemen Pinjaman:")
        print("1. Tambah Aplikasi Pinjaman")
        print("2. Lihat Semua Aplikasi Pinjaman")
        print("3. Perbarui Aplikasi Pinjaman")
        print("4. Hapus Aplikasi Pinjaman")
        print("5. Lihat Data yang Telah Dihapus")
        print("6. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            create_loan(user_id)
        elif choice == '2':
            read_loans()
        elif choice == '3':
            update_loan(user_id)
        elif choice == '4':
            delete_loan(user_id)
        elif choice == '5':
            view_deleted_loans()            
        elif choice == '6':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid, coba lagi.")

# Jalankan program
if __name__ == "__main__":
    main()
