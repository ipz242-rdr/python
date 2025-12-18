import csv
import os
import sys
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List


class KmrCsv:
    ref = "default.csv"
    num = 0

    def __init__(self, ref=None, num=None):
        self.ref = ref if ref else KmrCsv.ref
        self.num = num if num else KmrCsv.num
        self.data: List[Dict] = []

    def read_csv(self):
        self.data = []

        if not os.path.exists(self.ref):
            print(f"Помилка: Файл '{self.ref}' не знайдено.")
            print("Переконайтеся, що файл знаходиться в тій самій папці, що і програма.")
            sys.exit(1)

        def parse_time_to_minutes(t: str) -> float:
            t = t.strip()
            parts = t.split()
            minutes = 0
            seconds = 0
            if "хв" in parts:
                i = parts.index("хв")
                minutes = int(parts[i - 1])
            if "сек" in parts:
                i = parts.index("сек")
                seconds = int(parts[i - 1])
            return minutes + seconds / 60.0

        try:
            with open(self.ref, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)

                for row in reader:
                    if not row or not row[0]:
                        continue

                    clean_row = {}
                    try:
                        clean_row['Student ID'] = row[0].strip()

                        clean_row['Time'] = parse_time_to_minutes(row[3])

                        grade_str = row[4].replace('"', '').replace(',', '.')
                        clean_row['Grade'] = float(grade_str)

                        q_index = 1
                        for val in row[5:]:
                            val = val.strip().replace('"', '')
                            if val == '-' or val == '':
                                score = 0.0
                            else:
                                score = float(val.replace(',', '.'))
                            clean_row[f'Q{q_index}'] = score
                            q_index += 1
                    except (ValueError, IndexError):
                        continue

                    self.data.append(clean_row)

        except Exception as e:
            print(f"Критична помилка при читанні файлу: {e}")
            sys.exit(1)

    def file_info(self):
        if not self.data:
            self.read_csv()
        print(f"КМР №{self.num} ('{self.ref}'): Завантажено {len(self.data)} записів.")


class Statistic(KmrCsv):
    def avg_stat(self) -> Tuple[float, ...]:
        if not self.data:
            self.read_csv()
        if not self.data:
            return ()

        question_keys = sorted([k for k in self.data[0].keys() if k.startswith('Q')])

        results = []
        total_students = len(self.data)
        if total_students == 0:
            return ()

        for q in question_keys:
            values = [student.get(q, 0.0) for student in self.data]
            max_val = max(values) if values else 0.0
            total = sum(values)
            if max_val > 0:
                percent = (total / (len(values) * max_val)) * 100
            else:
                percent = 0.0
            results.append(round(percent, 2))
        return tuple(results)

    def marks_stat(self) -> Dict[float, int]:
        if not self.data:
            self.read_csv()
        counts: Dict[float, int] = {}
        for student in self.data:
            g = student['Grade']
            counts[g] = counts.get(g, 0) + 1
        return dict(sorted(counts.items()))

    def marks_per_time(self) -> Dict[str, float]:
        if not self.data:
            self.read_csv()
        results: Dict[str, float] = {}
        for student in self.data:
            s_id = student['Student ID']
            grade = student['Grade']
            time = student['Time']
            speed = grade / time if time > 0 else 0
            results[s_id] = round(speed, 3)
        return results

    def best_marks_per_time(self, bottom_margin: float, top_margin: float) -> Tuple:
        if not self.data:
            self.read_csv()

        filtered_students = [
            s for s in self.data if bottom_margin <= s['Grade'] <= top_margin
        ]

        scored_list = []
        for s in filtered_students:
            speed = s['Grade'] / s['Time'] if s['Time'] > 0 else 0
            scored_list.append((s['Student ID'], s['Grade'], round(speed, 3)))

        scored_list.sort(key=lambda x: x[2], reverse=True)
        return tuple(scored_list[:5])


class Plots:
    cat = "Results_KMR_Img"

    def set_cat(self, folder_name: str):
        self.cat = folder_name
        if not os.path.exists(self.cat):
            os.makedirs(self.cat)

    def avg_plot(self, avg_data: Tuple[float, ...], filename="avg_plot.png"):
        if not avg_data:
            print("Немає даних для графіка avg_plot")
            return

        plt.figure(figsize=(10, 6))
        questions = [f"Q{i + 1}" for i in range(len(avg_data))]

        plt.bar(questions, avg_data, color='skyblue', edgecolor='black')
        plt.title('Відсоток правильних відповідей')
        plt.ylabel('Відсотки %')
        plt.ylim(0, 105)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        for i, val in enumerate(avg_data):
            plt.text(i, val + 1, f"{val}%", ha='center')

        save_path = os.path.join(self.cat, filename)
        plt.savefig(save_path)
        plt.close()
        print(f"Графік збережено: {save_path}")

    def marks_plot(self, marks_data: Dict[float, int], filename="marks_plot.png"):
        if not marks_data:
            print("Немає даних для графіка marks_plot")
            return

        plt.figure(figsize=(10, 6))
        grades = [str(k) for k in marks_data.keys()]
        counts = list(marks_data.values())

        plt.bar(grades, counts, color='salmon', edgecolor='black')
        plt.title('Розподіл оцінок')
        plt.xlabel('Оцінка')
        plt.ylabel('Кількість студентів')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        save_path = os.path.join(self.cat, filename)
        plt.savefig(save_path)
        plt.close()
        print(f"Графік збережено: {save_path}")

    def best_marks_plot(self, best_data: Tuple, filename="best_speed.png"):
        if not best_data:
            print("Немає даних для графіка best_marks_plot")
            return

        plt.figure(figsize=(10, 6))
        ids = [item[0] for item in best_data]
        speeds = [item[2] for item in best_data]

        plt.bar(ids, speeds, color='lightgreen', edgecolor='black')
        plt.title('Топ-5 студентів за швидкістю (Бал/хв)')
        plt.ylabel('Балів за хвилину')

        for i, v in enumerate(speeds):
            plt.text(i, v + 0.1, str(v), ha='center')

        save_path = os.path.join(self.cat, filename)
        plt.savefig(save_path)
        plt.close()
        print(f"Графік збережено: {save_path}")


class KmrWork(Statistic, Plots):
    kmrs: Dict[int, str] = {}
    cat = "Results_KMR_Img"

    def __init__(self, ref: str, num: int):
        KmrCsv.__init__(self, ref, num)
        self.set_cat(KmrWork.cat)
        self.read_csv()


if __name__ == "__main__":
    my_filename = "marks2.lab11.csv"

    print(f"--- Обробка файлу {my_filename} ---")
    kmr_work = KmrWork(my_filename, 2)

    kmr_work.file_info()

    avg_stats = kmr_work.avg_stat()
    kmr_work.avg_plot(avg_stats, "lab11_avg_plot.png")

    marks_stats = kmr_work.marks_stat()
    kmr_work.marks_plot(marks_stats, "lab11_marks_plot.png")

    best_results = kmr_work.best_marks_per_time(6.0, 10.0)
    print(f"\nТоп-5 результатів (швидкість): {best_results}")
    kmr_work.best_marks_plot(best_results, "lab11_best_speed.png")

    print("\nГотово! Графіки збережено в папку 'Results_KMR_Img'.")
