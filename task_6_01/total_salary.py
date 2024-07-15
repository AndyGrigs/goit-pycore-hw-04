def total_salary(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            total_salary = 0
            developer_count = 0

            for line in file:
                try:
                    _, salary_str = line.strip().split(',')
                    total_salary += int(salary_str)
                    developer_count += 1
                except ValueError:
                    print(f"Помилка обробки рядка {line.strip()}")
            
            average_salary = total_salary / developer_count if developer_count else 0
            
            return total_salary, int(average_salary)
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    

# Приклад використання функції:
path_to_file = "salary_file.txt"
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
