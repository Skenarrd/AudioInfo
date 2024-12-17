from pydub import AudioSegment
from pydub.utils import mediainfo
import os

def get_audio_info(file_path: str) -> None:
    """
    Отображает основную информацию об аудиофайле.
    
    Args:
        file_path (str): Путь к аудиофайлу
    """
    try:
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл '{file_path}' не найден")
            return

        # Информация о файле
        info = mediainfo(file_path)
        
        # Загружаем аудио для получения длительности
        audio = AudioSegment.from_file(file_path)
        
        # Выводим основную информацию
        print("\n=== Информация об аудиофайле ===")
        print(f"Имя файла: {os.path.basename(file_path)}")
        print(f"Формат: {info.get('format_name', 'Неизвестно')}")
        print(f"Длительность: {round(audio.duration_seconds, 2)} секунд")
        print(f"Частота дискретизации: {info.get('sample_rate', 'Неизвестно')} Гц")
        print(f"Битрейт: {info.get('bit_rate', 'Неизвестно')} бит/с")
        print(f"Каналы: {info.get('channels', 'Неизвестно')}")
        print(f"Размер файла: {round(os.path.getsize(file_path) / (1024 * 1024), 2)} МБ")
        
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")

if __name__ == "__main__":
    file_path = input("Введите путь к аудиофайлу: ")
    get_audio_info(file_path)
