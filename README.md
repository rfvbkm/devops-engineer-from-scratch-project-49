# devops-engineer-from-scratch-project-49

## Сборка и запуск

Нужны [Python](https://www.python.org/) 3.10+ и менеджер пакетов [uv](https://docs.astral.sh/uv/).

После клонирования репозитория установите зависимости в виртуальное окружение (команда полезна и при первом клонировании, и если окружение сбрасывали):

```bash
make install
# то же самое: uv sync
```

Собрать дистрибутивы пакета (wheel и sdist в каталоге `dist/`):

```bash
make build
# то же самое: uv build
```

Запуск игр из исходников через `uv` (после `make install`):

```bash
uv run brain-games
uv run brain-even
uv run brain-calc
uv run brain-gcd
uv run brain-progression
uv run brain-prime
```

Установка собранного wheel как CLI-утилит в окружение `uv tool` (сначала выполните `make build`):

```bash
make package-install
# то же самое: uv tool install dist/*.whl
```

После этого команды `brain-games`, `brain-even` и остальные будут доступны в `PATH` (как правило, рядом с другими утилитами `uv`).

Проверка линтером:

```bash
make lint
```

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

### Demo

#### Brain Even

[![asciicast](https://asciinema.org/a/lGqcQgHQPkl4yFY4.svg)](https://asciinema.org/a/lGqcQgHQPkl4yFY4)

#### Brain Calc

[![asciicast](https://asciinema.org/a/PkhaApo2HLYuwHdS.svg)](https://asciinema.org/a/PkhaApo2HLYuwHdS)

#### Brain GCD

[![asciicast](https://asciinema.org/a/xkm77u9Y55TNClo4.svg)](https://asciinema.org/a/xkm77u9Y55TNClo4)

#### Brain Progression

[![asciicast](https://asciinema.org/a/XIMpixsRGoYrMmw6.svg)](https://asciinema.org/a/XIMpixsRGoYrMmw6)

#### Brain Prime

[![asciicast](https://asciinema.org/a/OnzxE9ltpbyKuR4U.svg)](https://asciinema.org/a/OnzxE9ltpbyKuR4U)
