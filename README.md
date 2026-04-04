# devops-engineer-from-scratch-project-49

## Badges

### Hexlet tests and linter status

[![Actions Status](https://github.com/rfvbkm/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/rfvbkm/devops-engineer-from-scratch-project-49/actions)

### SonarQube Quality Gate Status

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=rfvbkm_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=rfvbkm_devops-engineer-from-scratch-project-49)

## О проекте

Консольный пакет **Brain Games**: набор логических и математических мини-игр («проверка на чётность», калькулятор, НОД, арифметическая прогрессия, простые числа и др.). Общий цикл вопрос–ответ вынесен в модуль `brain_games.engine`, правила каждой игры — в пакете `brain_games.games`, точки входа CLI — в `brain_games.scripts`.

## Требования

- [Python](https://www.python.org/) 3.10+
- [uv](https://docs.astral.sh/uv/) для зависимостей и запуска

## Установка и запуск

Клонирование репозитория и установка зависимостей в виртуальное окружение (после смены ветки или удаления `.venv` выполните снова):

```bash
make install
# эквивалент: uv sync
```

Сборка wheel и sdist в каталог `dist/`:

```bash
make build
# эквивалент: uv build
```

**Запуск из исходников** (через окружение проекта):

```bash
uv run brain-games
uv run brain-even
uv run brain-calc
uv run brain-gcd
uv run brain-progression
uv run brain-prime
```

**Установка собранного пакета как набора команд** (после `make build`):

```bash
make package-install
# эквивалент: uv tool install dist/*.whl
```

После `uv tool install` команды доступны в `PATH` **без** префикса `uv run`, например:

```text
brain-calc
brain-prime
```

Линтер:

```bash
make lint
```

## Демонстрации (asciinema)

Ниже — встроенные записи по шагам курса: сценарии игр, в том числе успешное и неуспешное завершение. Отдельные записи на [asciinema.org](https://asciinema.org/) также демонстрируют установку и игровой процесс.

### Brain Even

[![asciicast](https://asciinema.org/a/lGqcQgHQPkl4yFY4.svg)](https://asciinema.org/a/lGqcQgHQPkl4yFY4)

### Brain Calc

[![asciicast](https://asciinema.org/a/PkhaApo2HLYuwHdS.svg)](https://asciinema.org/a/PkhaApo2HLYuwHdS)

### Brain GCD

[![asciicast](https://asciinema.org/a/xkm77u9Y55TNClo4.svg)](https://asciinema.org/a/xkm77u9Y55TNClo4)

### Brain Progression

[![asciicast](https://asciinema.org/a/XIMpixsRGoYrMmw6.svg)](https://asciinema.org/a/XIMpixsRGoYrMmw6)

### Brain Prime

[![asciicast](https://asciinema.org/a/OnzxE9ltpbyKuR4U.svg)](https://asciinema.org/a/OnzxE9ltpbyKuR4U)
