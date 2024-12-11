def student_data(name: str, grade: int):
    student = {name: 'ivan', grade: 90}


    while True:
        print('add, update, delete, view, exit')
        choice = input('masukkan pilihan : ')

        if choice == 'add':
            name = input('masukkan nama ')
            grade = input('masukkan nilai ')
            