// task6.cpp - JSON валидатор
#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <windows.h>  // для SetConsoleOutputCP

class JsonValidator {
public:
    bool validateFile(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cout << "Ошибка: файл '" << filename << "' не найден" << std::endl;
            return false;
        }

        std::string jsonContent;
        std::string line;
        while (std::getline(file, line)) {
            jsonContent += line + "\n";
        }
        file.close();

        std::cout << "Проверка файла: " << filename << std::endl;
        return validateString(jsonContent);
    }

    bool validateString(const std::string& json) {
        std::stack<char> brackets;
        bool inQuotes = false;

        for (size_t i = 0; i < json.length(); i++) {
            char c = json[i];

            // Обработка кавычек
            if (c == '"') {
                if (i == 0 || json[i - 1] != '\\') {
                    inQuotes = !inQuotes;
                }
            }

            // Если внутри кавычек - пропускаем проверку скобок
            if (inQuotes) {
                continue;
            }

            // Проверка скобок
            if (c == '{' || c == '[') {
                brackets.push(c);
            }
            else if (c == '}') {
                if (brackets.empty() || brackets.top() != '{') {
                    std::cout << "  [ERROR] Непарная '}' на позиции " << i << std::endl;
                    return false;
                }
                brackets.pop();
            }
            else if (c == ']') {
                if (brackets.empty() || brackets.top() != '[') {
                    std::cout << "  [ERROR] Непарная ']' на позиции " << i << std::endl;
                    return false;
                }
                brackets.pop();
            }
        }

        // Проверяем, что все кавычки закрыты
        if (inQuotes) {
            std::cout << "  [ERROR] Непарные кавычки" << std::endl;
            return false;
        }

        // Проверяем, что все скобки закрыты
        if (!brackets.empty()) {
            std::cout << "  [ERROR] Не все скобки закрыты" << std::endl;
            return false;
        }

        std::cout << "  [OK] ВАЛИДНЫЙ JSON" << std::endl;
        return true;
    }
};

int main() {
    // Устанавливаем кодировку консоли для русского языка
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);

    std::cout << "========================================" << std::endl;
    std::cout << "JSON VALIDATOR (C++)" << std::endl;
    std::cout << "========================================" << std::endl;

    JsonValidator validator;

    // Список файлов для проверки
    std::string files[] = {
        "classrooms.json",
        "acmp_tasks.json"
    };

    bool allValid = true;

    std::cout << "\n--- ПРОВЕРКА ФАЙЛОВ ---" << std::endl;
    for (const auto& filename : files) {
        std::cout << std::endl;
        if (!validator.validateFile(filename)) {
            allValid = false;
        }
    }

    // Тестовые примеры
    std::cout << "\n--- ТЕСТОВЫЕ ПРИМЕРЫ ---" << std::endl;

    std::string validJson = "{\"name\": \"Student\", \"age\": 20}";
    std::string invalidJson = "{name: Student, age: 20}";
    std::string validArray = "[1, 2, 3, 4, 5]";
    std::string invalidArray = "[1, 2, 3, 4, 5";

    std::cout << "\nTest 1 (valid object):" << std::endl;
    std::cout << "  JSON: " << validJson << std::endl;
    validator.validateString(validJson);

    std::cout << "\nTest 2 (invalid - no quotes):" << std::endl;
    std::cout << "  JSON: " << invalidJson << std::endl;
    validator.validateString(invalidJson);

    std::cout << "\nTest 3 (valid array):" << std::endl;
    std::cout << "  JSON: " << validArray << std::endl;
    validator.validateString(validArray);

    std::cout << "\nTest 4 (invalid - missing bracket):" << std::endl;
    std::cout << "  JSON: " << invalidArray << std::endl;
    validator.validateString(invalidArray);

    std::cout << "\n========================================" << std::endl;
    if (allValid) {
        std::cout << "RESULT: All files are VALID JSON" << std::endl;
    }
    else {
        std::cout << "RESULT: Some files have ERRORS" << std::endl;
    }
    std::cout << "========================================" << std::endl;

    std::cout << "\nPress Enter to exit...";
    std::cin.get();

    return 0;
}