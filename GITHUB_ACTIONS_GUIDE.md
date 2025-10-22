# 🤖 GitHub Actions - Автоматическая сборка и релиз

## Что происходит при создании тега

Когда вы создаёте тег версии (например, `v1.0.2`), GitHub Actions автоматически:

### 1️⃣ Сборка Windows
- ✅ Собирает portable версию (ZIP)
- ✅ Собирает installer с Inno Setup (EXE)
- ✅ Создаёт SHA256 checksums

### 2️⃣ Сборка Linux
- ✅ Собирает AppImage (универсальный Linux пакет)
- ✅ Создаёт checksums

### 3️⃣ Сборка macOS
- ✅ Собирает .app bundle
- ✅ Создаёт DMG installer
- ✅ Создаёт checksums

### 4️⃣ Публикация релиза
- ✅ Создаёт GitHub Release
- ✅ Загружает все артефакты
- ✅ Добавляет описание с инструкциями по установке

## Как запустить автосборку

```bash
# 1. Убедитесь что все изменения закоммичены
git add .
git commit -m "Your changes"
git push

# 2. Создайте тег версии
git tag v1.0.2

# 3. Запушьте тег
git push origin v1.0.2
```

## Проверка статуса сборки

1. Откройте: https://github.com/bobberdolle1/TerraForge-Studio/actions
2. Найдите workflow "Build Multi-Platform Releases"
3. Кликните на запущенный workflow для деталей

## Время сборки

| Платформа | Время |
|-----------|-------|
| Windows   | ~10-15 мин |
| Linux     | ~15-20 мин |
| macOS     | ~20-25 мин |
| **Всего** | ~25-30 мин |

## Результаты

После успешной сборки в [Releases](https://github.com/bobberdolle1/TerraForge-Studio/releases) появится:

```
TerraForge-Studio-v1.0.2-Windows-Portable.zip
TerraForge-Studio-Setup-v1.0.2.exe
TerraForge-Studio-v1.0.2-Linux-x86_64.AppImage
TerraForge-Studio-v1.0.2-macOS.dmg
+ SHA256 checksums для каждого файла
```

## Troubleshooting

### Workflow не запустился

**Причина:** Workflow файл не был в репозитории на момент создания тега

**Решение:**
```bash
# Удалить старый тег
git tag -d v1.0.2
git push origin :refs/tags/v1.0.2

# Создать новый тег
git tag v1.0.2
git push origin v1.0.2
```

### Сборка упала с ошибкой

1. Проверьте логи в GitHub Actions
2. Исправьте ошибки
3. Создайте новый тег:
```bash
git tag v1.0.3
git push origin v1.0.3
```

### macOS сборка не работает

macOS сборка может упасть если:
- Отсутствуют зависимости
- Проблемы с code signing

Временное решение - отключите macOS в workflow:
```yaml
# Закомментируйте в .github/workflows/build-multiplatform.yml
# build-macos:
#   ...
```

## Ручная сборка (если Actions не работает)

### Windows
```powershell
.\desktop\build_all.ps1 -Installer -Release
```

### Linux (требует Linux машину или WSL)
```bash
./desktop/build_linux.sh
```

### macOS (требует macOS машину)
```bash
./desktop/build_macos.sh
```

## Настройка workflow

Файл: `.github/workflows/build-multiplatform.yml`

Основные секции:
- `on:` - когда запускать (теги v*.*.*)
- `jobs:` - какие платформы собирать
- `steps:` - шаги сборки

Измените версию Node.js:
```yaml
- name: Set up Node.js
  uses: actions/setup-node@v4
  with:
    node-version: '20'  # <-- здесь
```

Измените версию Python:
```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.13'  # <-- здесь
```

## Секреты (если нужны)

Для code signing или публикации в stores добавьте секреты:

1. GitHub → Settings → Secrets and variables → Actions
2. New repository secret
3. Используйте в workflow:
```yaml
env:
  SIGNING_KEY: ${{ secrets.SIGNING_KEY }}
```

## Следующие шаги

После успешной сборки:

1. ✅ Проверьте релиз: https://github.com/bobberdolle1/TerraForge-Studio/releases
2. ✅ Скачайте и протестируйте каждую платформу
3. ✅ Обновите CHANGELOG.md
4. ✅ Анонсируйте релиз

---

**Готово!** Теперь каждый тег автоматически создаёт multi-platform релиз! 🚀
