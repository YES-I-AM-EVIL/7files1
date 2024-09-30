from cook_book import cook_book

def write_recipes_to_file(cook_book, filename):
    """Функция для записи рецептов из словаря cook_book в файл в нужном формате."""
    with open(filename, 'w', encoding='utf-8') as file:
        for dish, ingredients in cook_book.items():
            file.write(f"{dish}\n")  # Название блюда
            file.write(f"{len(ingredients)}\n")  # Количество ингредиентов
            for ingredient in ingredients:
                # Записываем ингредиенты в формате: Название ингредиента | Количество | Единица измерения
                file.write(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n")
            file.write("\n")  # Добавляем пустую строку после каждого блюда

# Пример использования программы
if __name__ == '__main__':
    output_file = 'recipes.txt'  # Имя файла, куда записываются рецепты
    write_recipes_to_file(cook_book, output_file)
    print(f"Рецепты успешно записаны в {output_file}")