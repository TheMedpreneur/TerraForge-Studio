# 🗺️ RealWorldMapGen-BNG

**ИИ-генератор карт реального мира для BeamNG.drive**

Полноценный инструмент для генерации детализированных и функциональных карт реальных локаций для BeamNG.drive с автоматической генерацией инфраструктуры (дороги, светофоры, парковки, здания, растительность) на основе ИИ-анализа спутниковых снимков и данных OpenStreetMap.

## ✨ Возможности

- 🌍 **Интеграция реальных данных**: Извлечение географических данных из OpenStreetMap для любой локации
- 🤖 **ИИ-анализ**: Использует Qwen3-VL и Qwen3-Coder через Ollama для интеллектуального анализа местности
- 🏔️ **Генерация heightmap**: Создание детальных данных о высоте из источников SRTM
- 🛣️ **Генерация дорожной сети**: Автоматическое создание дорог с правильными типами, полосами и материалами
- 🚦 **Дорожная инфраструктура**: Размещение светофоров и создание парковок на основе данных OSM
- 🏢 **Размещение зданий**: Извлечение и позиционирование зданий с информацией о высоте
- 🌳 **Распределение растительности**: Генерация деревьев и зон растительности на основе анализа местности
- 🎮 **Экспорт в BeamNG.drive**: Вывод всех данных в форматы, совместимые с BeamNG.drive
- 🌐 **Веб-интерфейс**: Интерактивный выбор области с интеграцией Leaflet
- 🐳 **Поддержка Docker**: Полная контейнеризация с Docker Compose

## 🚀 Быстрый старт

### Требования

- **Docker & Docker Compose** (для бэкенда и фронтенда)
- **Ollama** (локальная установка - скачать с https://ollama.ai)
- **Python 3.13+** (для локальной разработки)
- **Poetry** (для управления зависимостями)
- **Git**

### Установка через Docker (Рекомендуется)

1. **Клонируйте репозиторий**:
   ```bash
   git clone <url-репозитория>
   cd RealWorldMapGen-BNG
   ```

2. **Запустите автоматическую установку**:
   
   **Windows (PowerShell)**:
   ```powershell
   .\setup.ps1
   ```
   
   **Linux/Mac**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Откройте веб-интерфейс**:
   Перейдите в браузере: `http://localhost:8080`

### Ручная установка

1. **Создайте файл .env**:
   ```bash
   cp .env.example .env
   ```

2. **Запустите Docker Compose**:
   ```bash
   docker-compose up -d
   ```

3. **Установите и запустите Ollama локально**:
   - Скачайте с https://ollama.ai
   - Установите и запустите: `ollama serve`
   - Cloud модели (qwen3-vl:235b-cloud, qwen3-coder:480b-cloud) используются автоматически через API

## 📖 Использование

### Веб-интерфейс

1. **Откройте** `http://localhost:8080` в браузере
2. **Выберите область** на карте с помощью инструмента прямоугольника
3. **Настройте параметры**:
   - Название карты
   - Разрешение heightmap (1024, 2048, 4096)
   - Включение/отключение функций (ИИ, дороги, светофоры, здания и т.д.)
4. **Нажмите "Generate Map"**
5. **Скачайте** сгенерированные файлы после завершения

### API

#### Генерация карты

```bash
curl -X POST "http://localhost:8000/api/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "moya_karta",
    "bbox": {
      "north": 55.7558,
      "south": 55.7508,
      "east": 37.6173,
      "west": 37.6123
    },
    "resolution": 2048,
    "enable_ai_analysis": true,
    "enable_roads": true,
    "enable_traffic_lights": true,
    "enable_parking": true,
    "enable_buildings": true,
    "enable_vegetation": true
  }'
```

#### Проверка статуса системы

```bash
curl http://localhost:8000/api/health
```

#### Список сгенерированных карт

```bash
curl http://localhost:8000/api/maps
```

## 🎮 Импорт в BeamNG.drive

1. **Найдите** сгенерированную карту в директории `output/<имя_карты>/`
2. **Скопируйте файлы** в папку уровней BeamNG.drive:
   ```
   <BeamNG.drive>/levels/<имя_карты>/
   ```
3. **Необходимые файлы**:
   - `main.level.json` - Конфигурация уровня
   - `<имя_карты>_heightmap.png` - Heightmap ландшафта
   - `roads.json` - Данные дорожной сети
   - `objects.json` - Здания и растительность
   - `traffic.json` - Светофоры и парковки
   - `info.json` - Метаданные карты

4. **Запустите BeamNG.drive** и загрузите свою карту

## ⚙️ Конфигурация

Настройте файл `.env`:

```env
# Настройки Ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_VISION_MODEL=qwen3-vl:235b-cloud
OLLAMA_CODER_MODEL=qwen3-coder:480b-cloud

# Настройки генерации карт
DEFAULT_RESOLUTION=2048
MAX_AREA_KM2=100.0

# Настройки обработки
ENABLE_AI_ANALYSIS=true
PARALLEL_PROCESSING=true
MAX_WORKERS=4
```

## 🏗️ Структура проекта

```
RealWorldMapGen-BNG/
├── realworldmapgen/          # Основной Python-пакет
│   ├── ai/                   # Интеграция ИИ (Ollama)
│   ├── osm/                  # Извлечение данных OSM
│   ├── elevation/            # Генерация heightmap
│   ├── exporters/            # Экспорт в BeamNG.drive
│   ├── api/                  # FastAPI бэкенд
│   └── generator.py          # Главный оркестратор
├── frontend/                 # Веб-интерфейс
├── docker-compose.yml        # Docker оркестрация
└── pyproject.toml            # Poetry зависимости
```

## 🛠️ Разработка

### Локальная разработка

1. **Установите Poetry**:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Установите зависимости**:
   ```bash
   poetry install
   ```

3. **Запустите бэкенд**:
   ```bash
   poetry run uvicorn realworldmapgen.api.main:app --reload
   ```

### Тестирование

```bash
poetry run pytest
```

### Форматирование кода

```bash
poetry run black realworldmapgen/
poetry run ruff check realworldmapgen/
```

## 📦 Основные зависимости

- **FastAPI** - Современный веб-фреймворк
- **osmnx** - Извлечение данных OpenStreetMap
- **ollama** - Интеграция с ИИ-моделями
- **geopandas** - Обработка геопространственных данных
- **numpy**, **Pillow**, **rasterio** - Обработка изображений и данных

## 🐛 Известные проблемы

- **Большие области**: Обработка областей >50 км² требует значительной памяти
- **Модели Ollama**: Первая загрузка моделей большая (50GB+ суммарно)
- **Ограничения OSM**: Частые запросы могут быть ограничены
- **Данные о высоте**: Первая загрузка может быть медленной

## 📝 Roadmap

- [ ] Реализация загрузки и анализа реальных спутниковых снимков
- [ ] Поддержка пользовательских префабов объектов
- [ ] Генерация маршрутов трафика
- [ ] Поддержка пользовательских текстур и материалов
- [ ] Генерация превью карты
- [ ] Пакетная обработка нескольких областей
- [ ] Инкрементальное обновление существующих карт

## 📄 Лицензия

MIT License - см. файл LICENSE

## 🙏 Благодарности

- Вдохновлено проектом [unrealheightmap](https://github.com/manticorp/unrealheightmap)
- Создано с использованием [osmnx](https://github.com/gboeing/osmnx)
- Работает на [Ollama](https://ollama.ai) и моделях Qwen
- Данные карт © [OpenStreetMap](https://www.openstreetmap.org) contributors

---

**Сделано с ❤️ для сообщества BeamNG.drive**
